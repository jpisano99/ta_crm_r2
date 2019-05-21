#
# Basic mod_WSGI file for AWS which REQUIRES the variable "application" for the flask app
#
from my_app import app as application

if __name__ == "__main__":
    application.run(debug=False)