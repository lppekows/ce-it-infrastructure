#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import os

url = URL.create(
    drivername="mariadb",
    username="root",
    password=os.environ["MARIADB_ROOT_PASSWORD"],
    host=os.environ["FQDN"],
    database=os.environ["MARIADB_DATABASE"],
    port=3306
)

engine = create_engine(url)

if __name__ == '__main__':
    my_query = f"SHOW TABLES;"
    tables   = pd.read_sql_query(sql=my_query, con=engine)
    for _,tvalue in tables.iterrows():
        table = tvalue.values[0]
    
        my_query = f"SHOW COLUMNS FROM {table};"
        columns = pd.read_sql_query(sql=my_query, con=engine)
        for _,value in columns.iterrows():
            name = value['Field']
            if name.endswith('ID') and not name.startswith(table):
                foreignTable = name[:-2]
                print(f"ALTER TABLE {table} ADD CONSTRAINT FOREIGN KEY ({name}) REFERENCES {foreignTable} ({name});")


