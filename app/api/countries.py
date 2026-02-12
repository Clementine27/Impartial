from app.api import bp
from flask import request
from app.models import Country
from app import db


# all countries by filtering 
@bp.route("/countries", methods = ["GET"])
def getCountries(): 
    query = db.select(Country)
    
    continent = request.args.get("continent")
    # TODO get events from country 
    events = request.args.get("events")

    if continent is not None: 
        query = query.where(Country.continent == continent)
    
    if events is not None: 
        query = query.where()
        # return the events that dont have any parents 
    countries = db.session.scalars(query).all()
    return  [country.to_dict() for country in countries]

# get country by name/name variations 
@bp.route("/countries/<int:id>", methods = ["GET"])
def getCountry(id): 

    return db.get_or_404(Country, id).to_dict()


# (opt) theme-economic events that happened 
# during period-(the cold war) that involves  
# countries-france and vn, where they nations disagreed 
# on summary-how much does oil cost  

