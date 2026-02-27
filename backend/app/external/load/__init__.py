from . import countries_conti
from flask import current_app
import pandas as pd 
from app.models import Country, Event
from app.extentions import db 
from ..transform import *

def load_countries(): 
    with current_app.app_context(): 
        try: 
            file = pd.read_csv(countries_conti)
            
            for i, row in file.iterrows: 
                record = Country(**{
                    "name": row["Country"], 
                    "continent": row["Continent"]   
                }
            )
                db.session.add(record)
        except: 
            db.session.rollback()
            
        db.session.commit()


def load_events(rows): 
    for row in rows:
        event = Event.query.filter_by(title=row['course_title'])

        if event :
            db.session.add(event)

    
    db.session.commit()




def run_all_loads(): 
    load_countries()
    sources = ["wikipedia, britanica"]
    
    load_events("britanica")
    pass 