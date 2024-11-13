#!/usr/bin/env python3

import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

import urllib.parse
import mariadb

class RESTHandler(BaseHTTPRequestHandler):
    def send_result(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        outs = json.dumps(data, separators=(',', ':'), default=str)
        self.wfile.write(outs.encode('utf-8'))

    def send_success(self, data):
        self.send_result(200,data)

    def send_failure(self, data):
        self.send_result(500,data)

    def parameters(self):
        try:
            length = int(self.headers['Content-Length'])
            jdata  = self.rfile.read(length) 
            data   = json.loads(jdata)
        except:
            data = None

        url_info        = urllib.parse.urlparse(self.path)
        path_components = url_info.path.split('/')
        table_name      = len(path_components) > 2 and path_components[2] or None
        primary_key     = len(path_components) > 3 and path_components[3] or None
        qs              = urllib.parse.parse_qs(url_info.query)
        
        return table_name, data, qs, primary_key

def format_value(v):
    try:
        return str(int(v))
    except:
        return f'"{v}"'

def makeGETorDEL(conn, prefix):
    def do_call(self):
        table_name,data,qs,pk = self.parameters()
        where = ""

        if qs:
            key = list(qs.keys())[0]
            val = qs[key][0]
            where = f"WHERE {key} = {format_value(val)}"
        elif pk:
            where = f"WHERE {table_name}ID = {format_value(pk)}"

        query = f"{prefix} FROM {table_name} {where}"
        print(query)
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute(query)
            result = cur.fetchall()
            print(f"{json.dumps(result,default=str)}")
            self.send_success(result) 
        except Exception as e: 
            print("Database error",e)
            self.send_failure({'error':str(e)})

    return do_call

def makePUT(conn):
    def do_PUT(self):
        table_name, data, _, _  = self.parameters()
        orderedKeys = sorted([k for k in data.keys() if data[k]])
        fields      = ','.join(orderedKeys)
        values      = ','.join([format_value(data[k]) for k in orderedKeys])

        try:
            cur = conn.cursor()
            print(f"INSERT INTO {table_name}({fields}) VALUES({values});")
            cur.execute(f"INSERT INTO {table_name}({fields}) VALUES({values});")
            self.send_success(data)
        except Exception as e: 
            print("Database error",e)
            self.send_failure({'error':str(e)})

    return do_PUT

def run():
    # Might want to move to a pool of connections
    # https://mariadb-corporation.github.io/mariadb-connector-python/pool.html
    try:
        conn = mariadb.connect(
            user="root",
            password=os.environ["MARIADB_ROOT_PASSWORD"],
            host=os.environ["FQDN"],
            database=os.environ["MARIADB_DATABASE"],
            port=3306
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    server_class  = HTTPServer
    handler_class = RESTHandler

    RESTHandler.do_GET    = makeGET(conn)
    RESTHandler.do_PUT    = makePUTorDEL(conn,"SELECT *")
    RESTHandler.do_DELETE = makePUTorDEL(conn,"DELETE")
    RESTHandler.do_POST   = makePUT(conn)

    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
   

if __name__ == '__main__':
    run()

