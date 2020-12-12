import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_meeting(mname,mcontent):
    con = sql.connect('meeting.db')
    cur = con.cursor()
    cur.execute('insert into mposts (mname, mcontent) values(?, ?)', (mname, mcontent))
    con.commit()
    con.close()

def get_meeting():
    con = sql.connect('meeting.db')
    cur = con.cursor()
    cur.execute('select * from mposts')
    mposts = cur.fetchall()
    return mposts
