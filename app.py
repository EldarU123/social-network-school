from flask import Flask, render_template, request, redirect, flash, url_for,session,abort
from flask_cors import CORS
from cmodels import create_parents, get_parents
from models import get_posts, create_post
from mmodels import get_meeting, create_meeting
import sqlite3 as sql
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging



app = Flask(__name__) 

CORS(app)





@app.route('/')
def index():

 
    return render_template('index.html')



@app.route('/parents.html', methods=['GET', 'POST'])
def parents():

    if request.method == 'GET':
        pass 

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('parents.html', posts=posts)
    


            


@app.route('/meeting.html', methods=['GET','POST'])
def meeting():

    if request.method == 'GET':
        pass
 
    if request.method == 'POST':
        mname = request.form.get('mname')
        mpost = request.form.get('mpost')
        create_meeting(mname, mpost)

    mposts = get_meeting()

    return render_template('meeting.html', mposts=mposts)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) 

