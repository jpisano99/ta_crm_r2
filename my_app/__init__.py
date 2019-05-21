# Get things started and initialized here
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from base64 import b64encode
from my_app.settings import db_config, ssh_config
from my_app.my_secrets import passwords

# Creating the Flask app must happen FIRST
app = Flask(__name__)


# Assign App Config Variables / Create a random token for Flask Session
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY'] = token

# Get the Passwords and Keys
print ("I have a DB Password: ",my_secrets.passwords["DB_PASSWORD"])
print ("I have an API Key: ",my_secrets.passwords["SS_TOKEN"])

#
# database configuration settings
#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+\
                                            db_config['USER']+\
                                        ':'+db_config['PASSWORD']+\
                                        '@'+db_config['HOST']+':3306/'+\
                                            db_config['DATABASE']

#
# # Create db for SQL Alchemy
db = SQLAlchemy(app)
#
# # Are we connected ?
# db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'port'"))
# for x in db_status:
#     db_port = x.values()
#
# db_status = (db.engine.execute("SHOW VARIABLES WHERE Variable_name = 'hostname'"))
# for x in db_status:
#     db_host = x.values()
#
# db_status = (db.engine.execute('SELECT USER()'))
# for x in db_status:
#     db_user = x.values()
#
# print('You are connected to MySQL Host '+db_host[1]+' on Port '+db_port[1]+' as '+db_user[0])


# Now get all views and models in
from my_app import views
from my_app import models

print('hello from __init__')

