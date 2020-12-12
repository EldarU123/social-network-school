import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_parents(pname,pcontent):
    con = sql.connect('calendar.db')
    cur = con.cursor()
    cur.execute('insert into calposts (pname, pcontent) values(?, ?)', (pname, pcontent))
    con.commit()
    con.close()

def get_parents():
    con = sql.connect('calendar.db')
    cur = con.cursor()
    cur.execute('select * from calposts')
    calposts = cur.fetchall()
    return calposts
