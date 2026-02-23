from app.api import bp
from flask import request
from app.models import Country
from app import db


@bp.route("/countries", methods = ["GET"])
def getCountries(): 
    query = db.select(Country)
    
    continent = request.args.get("continent")

    if continent is not None: 
        query = query.where(Country.continent == continent)
    
    countries = db.session.scalars(query).all()
    
    return  [country.to_dict() for country in countries]


# get country by name/name variations 
@bp.route("/countries/<int:id>", methods = ["GET"])
def getCountry(id): 

    return db.get_or_404(Country, id).to_dict()


