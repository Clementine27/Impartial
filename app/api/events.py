from app.api import bp 
from app.models import Events 
from app import db 
from flask import request 

@bp.route("/events", methods = ["GET"])
def getEvents():
    # get stuff from the database beforehand 
    query = db.select(Events)
    # configure filters 
    startYear = request.args.get("startYear")
    endYear = request.args.get("endYear")
    theme = request.args.get("theme")
    countries = request.args.get("countries")

    summary = request.args.get("q")
    childEvents = request.args.get("childEvents")
    # parentEvents = request.args.get("parentEvents")
    
    # return applied filters
    query = query.where(Events.startYear >= startYear and Events.endYear <= endYear)
    query = query.where(Events.theme == theme)
    
    # return the list of countries assc w event (for frontend)
    
    # return all the child events of this event as a list 
    
    