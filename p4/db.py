#!/usr/bin/env python
# coding=utf-8

import sqlite3 as sqlite

db = sqlite.connect("test.db")

cur = db.cursor()

# CREATE TABLE

CREATE_TABLE_QUERY = "CREATE TABLE test(id INT)"

# execute create table query
cur.execute(CREATE_TABLE_QUERY)

# commit changes

db.commit()

# insert data to table
INSERT_QUERY = "INSERT INTO test(id) VALUES('{0}')"

cur.execute(INSERT_QUERY.format("12"))

# commit changes

db.commit()

# close connection
db.close()

