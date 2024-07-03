#!/usr/bin/env python

from fastapi import FastAPI

# Useful examples at 
# https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/
# https://mattermost.com/blog/building-a-crud-fastapi-app-with-sqlalchemy/

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import sqlalchemy 
import tables

url = URL.create(
    drivername="mariadb",
    username="root",
    password="abcde",
    host="127.0.0.1",
    database="dcc",
    port=3306
)

engine = create_engine(url)

tables.Base.metadata.create_all(engine)

session = sqlalchemy.orm.sessionmaker()
session.configure(bind=engine)
session = session()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DCC RESTful app"}

@app.get("/authors")
async def authors():
    authors_query = session.query(tables.Author)
    return authors_query.all()

