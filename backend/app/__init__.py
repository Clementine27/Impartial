
# import sys; print(sys.executable)

from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

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

    

# @app.shell_context_processor
# def make_shell_context(): 
#     return {'sa': sa, 'so': so, 'db': db, 'Country': Country, 'Events': Events}
