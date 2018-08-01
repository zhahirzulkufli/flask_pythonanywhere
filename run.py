# import flask instance (app) from flask_app.py
from flask_app import app

# import all functions in views.py to expose url
from views import *

# run the file/program
if __name__=='__main__':
    app.run(debug=True)
