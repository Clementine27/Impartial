import requests
from app.config import WIKIPEDIA_URL 
from flask import current_app
import pandas as pd
from app.extentions import db 


def get_events(country): 
    """
    get the events wiki claim to exist in a country's history
    include: 
    subsections names under history of a country wiki
    hyperlinks of events --> store as names to be worked on by transform later  
    
    Args: 
        country (str): country name 
    Returns:
        dict: dict of events for event entries 
    """
    params = {
        "action": "query", 
        "srsearch": country, 
        "srlimit": 1, 
        "format": "json", 
        "prop": "text"
    }
    response = requests.get(WIKIPEDIA_URL, params)
    
    return response 


def write_events(): 
    """
    for country in country_conti 
        get_evets(country)
        
    json.dump({file path }. response)
    """
    with current_app.app_context():         
        pass 

