import os
import sys
#import requests
import json

from flask import Flask, render_template,request, session, redirect ,url_for, flash
from flask_session import Session
from datetime import datetime

#from flask.ext.session import Session
from sqlalchemy import * #create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import * #scoped_session,sessionmaker

from werkzeug.debug import DebuggedApplication

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL")
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template('index.html')

app.run(debug=True)

@app.route("/signup")
def signup():
     return render_template('signup.html',path='./styles/css/styles.min.css')

@app.route("/registration",methods=["POST"])
def registration():
    fname = request.form.get("firstName")
    lname = request.form.get("lastName")
    email = request.form.get("email")
    pwd = request.get.form("password")
    print(email+" , "+fname+" , "+lname)
    return email+" , "+fname+" , "+lname

app.run(debug=True)

