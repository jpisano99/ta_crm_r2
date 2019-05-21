# Get things started and initialized here
import os
from base64 import b64encode

#Creating the Flask app must happen FIRST
from flask import Flask
app = Flask(__name__)

# Assign App Config Variables / Create a random token for Flask Session
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY']= token

# Get the Passwords and Keys
from my_app import my_secrets
print ("I have a DB Password: ",my_secrets.passwords["DB_PASSWORD"])
print ("I have an API Key: ",my_secrets.passwords["SS_TOKEN"])

# Add a database here
from flask_sqlalchemy import SQLAlchemy
#
# database configuration settings
#
db_config = dict(
    DATABASE = "cust_ref_db",
    USER     = "root",
    PASSWORD = my_secrets.passwords["DB_PASSWORD"],
    HOST     = "localhost"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Local connect to RaspPi (Stan)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+\
                                            db_config['USER']+\
                                        ':'+db_config['PASSWORD']+\
                                        '@'+db_config['HOST']+':3306/'+\
                                            db_config['DATABASE']

# Create db for SQL Alchemy
db = SQLAlchemy(app)

# Are we connected ?
db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'port'"))
for x in db_status:
    db_port = x.values()

db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'hostname'"))
for x in db_status:
    db_host = x.values()

db_status = (db.engine.execute('SELECT USER()'))
for x in db_status:
    db_user = x.values()

print('You are connected to MySQL Host '+db_host[1]+' on Port '+db_port[1]+' as '+db_user[0])



#Now get all views and models in
from my_app import views
from my_app import models

print ('hello from __init__')