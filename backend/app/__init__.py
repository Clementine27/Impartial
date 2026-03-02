from flask import Flask
from app.config import Config
from app.extentions import db, migrate
from app.external.extract.wikipedia import get_history


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
    
    from app.external.cli import register_etl_cli
    register_etl_cli(app)
    
    @app.shell_context_protector()
    def make_shell_context(): 
        from app.models import Country, Event
        return {'db': db, 'Country': Country, 'Event': Event}

    return app


def main():     
    # from config import Config
    # from external.extract import get_sections

    get_history("Vietnam")
    
    
# if __name__ == "__main__": 
#     main()
    
    