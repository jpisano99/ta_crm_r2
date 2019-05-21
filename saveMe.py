# Assign App Config Variables / Create a random token for Flask Session
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY'] = token

# Get the Passwords and Keys

print ("I have a DB Password: ",my_secrets.passwords["DB_PASSWORD"])
print ("I have an API Key: ",my_secrets.passwords["SS_TOKEN"])

# Add a database here
# Create a tunnel for MySQL to access PythonAnywhere externally
#
sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

tunnel = sshtunnel.SSHTunnelForwarder(
    ssh_config['ENDPOINT'],
    ssh_username=ssh_config['USER'], ssh_password=ssh_config['PASSWORD'],
    remote_bind_address=(ssh_config['REMOTE_BIND_ADDRESS'], ssh_config['REMOTE_BIND_PORT'] )
    )
tunnel.start()

#
# Construct the URI to PythonAnyWhere
#
db_uri = 'mysql+pymysql://' + \
            db_config['USER'] + \
            ':'+db_config['PASSWORD'] +\
            '@'+db_config['HOST']+':{}/' + \
            db_config['DATABASE'].format(tunnel.local_bind_port)

db_uri = db_uri.format(tunnel.local_bind_port)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

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