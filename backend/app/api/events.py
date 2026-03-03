from app.api import bp 
from app.models import Event, Theme, Country, events_table
from app import db 
from flask import request 
import datetime as dt

@bp.route("/events", methods = ["GET"])
def getEvents():
    query = db.select(Event)

    startYear = request.args.get("start")
    endYear = request.args.get("end")
    themes = request.args.get("themes")
    countries = request.args.get("countries")
    # TODO summary = request.args.get("q")
    eventIDs = request.args.get("ids")
    rootOnly = request.args.get("root_only")
    leafOnly = request.args.get("leaf_only")

    if startYear: 
        query = query.where(Event.start >= dt.date(int(startYear), 1, 1))
    if endYear: 
        query = query.where(Event.end <= dt.date(int(endYear), 12, 31))
    if themes: 
        themesList = [int(i) for i in themes.split(",")]
        query = query.join(Event.themes).where(Theme.id.in_(themesList)).distinct()
    if countries: 
        countriesList = [int(i) for i in countries.split(",")]
        query = query.join(Event.countries).where(Country.id.in_(countriesList)).distinct()
    if eventIDs: 
        eventIDsList = [int(i) for i in eventIDs.split(",")]
        query = query.where(Event.id.in_(eventIDsList)) 
    if rootOnly: 
        subquery = db.select(events_table.c.child_event)
        query = query.where(~Event.id.in_(subquery))

    if leafOnly: 
        subquery = db.select(events_table.c.parent_event)
        query = query.where(~Event.id.in_(subquery))

    events = db.session.scalars(query).all()
    return [event.to_dict() for event in events]

    
@bp.route("/events/<int:id>", methods = ["GET"])
def getEvent(id): 
    return db.get_or_404(Event, id).to_dict()


