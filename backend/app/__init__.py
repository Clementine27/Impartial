from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.extentions import db, migrate

def create_app(config_class = Config): 
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)


    from app import models
    
    from app.errors import bp as bp_errors  
    app.register_blueprint(bp_errors)
   
    from app.routes import bp as bp_main  
    app.register_blueprint(bp_main)

    from app.api import bp as bp_api
    app.register_blueprint(bp_api, url_prefix = "/api")
    
    return app
