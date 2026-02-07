from flask import Flask, render_template
app = Flask(__name__)

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

# DATABASE ------
# set up connection to db 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# SHELL CONTEXT ------
# @app.shell_context_processor
# def make_shell_context(): 
#     return {'sa': sa, 'so': so, 'db': db, 'Country': Country, 'Events': Events}


# ROUTES ------
# ex: 
# when an user request the below 2 urls via these 2 decorators 
@app.route("/")
    # route func from app module takes in the index() func as argument 
    # and does its little magic trick so that the first ar i.e. /index 
    # spits out output from func index
@app.route("/index")
# invoke this func 
def index(): 
    # return "hello there, gorgeous!"
    # user = {"username"}
    return render_template('index.html')




if __name__ == '__main__': 
    with app.app_context(): 
        db.create_all()
        
    app.run(debug=True)
    
    
    
