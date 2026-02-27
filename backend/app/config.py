import os 

basedir = os.path.dirname(__file__)

class Config:
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        
    WIKIPEDIA_URL = "https://en.wikipedia.org/w/api.php"

