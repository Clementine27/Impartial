from __future__ import annotations
from typing import Optional
from app import db
import sqlalchemy as sa 
import sqlalchemy.orm as so 
import json 
import datetime as dt 

association_table = sa.Table(
    "association_table",  
    db.Model.metadata, 
    sa.Column(
        "country_id", sa.ForeignKey("country.id"), primary_key= True), 
    sa.Column(
        "event_id", sa.ForeignKey("event.id"), primary_key= True )
)

themes_table = sa.Table(
    "themes_table", 
    db.Model.metadata, 
    sa.Column(
        "event_id", sa.ForeignKey("event.id"), primary_key = True), 
    sa.Column(
        "themes_id", sa.ForeignKey("theme.id"), primary_key= True)
)

events_table = sa.Table(
    "events_table", 
    db.Model.metadata, 
    sa.Column(
        "parent_event", sa.ForeignKey("event.id"), primary_key = True), 
    sa.Column(
        "child_event", sa.ForeignKey("event.id"), primary_key= True)
)

class Country(db.Model): 
    __tablename__ = "country"

    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    name: so.Mapped[str] = so.mapped_column(sa.String, unique = True, nullable= False)
    continent: so.Mapped[str] = so.mapped_column(sa.String, nullable= False)    
    events: so.Mapped[list[Event]] = so.relationship(secondary=association_table, back_populates="countries")

    def __repr__(self):
        return '<Country {}>'.format(self.name)
            
    def to_dict(self): 
        data = {
            "id": self.id, 
            "name": self.name, 
            "continent": self.continent
        }
        if self.events:             
            data["eventsID"] = [event.id for event in self.events]

        return data 

class Event(db.Model): 
    __tablename__ = "event"

    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    name: so.Mapped[str] = so.mapped_column(sa.String(50), nullable = False)
    start: so.Mapped[dt.date] = so.mapped_column(sa.Date, nullable = False)  
    end: so.Mapped[dt.date] = so.mapped_column(sa.Date, nullable = False)  
    
    themes: so.Mapped[list[Theme]] = so.relationship(secondary= themes_table)
    summary: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)
    countries: so.Mapped[list[Country]] = so.relationship(secondary=association_table, back_populates="events")
    
    # parents: so.Mappeed[list[Event]] = so.relationship(secondary= events_table, back_populates= "children")
    # children: so.Mappeed[list[Event]] = so.relationship(secondary= events_table, back_populates= "parents")
    
    children:  so.Mapped[list[Event]] = so.relationship('Event', 
                                                         secondary = (events_table.c.child_event == id), 
                                                         primaryjoin = (events_table.c.parent_event == id), 
    secondaryjoin = (Event.c.followed_id == id), 
    backref = db.backref('events_table', lazy = 'dynamic'), 
    lazy = 'dynamic')


    def __repr__(self):
        return '<Events {}>'.format(self.name)
    
    def to_dict(self): 
        data = {
            "name": self.name, 
            "start": self.start, 
            "end": self.end
        } 
        if self.countries: 
            data["countryIDs"] = [country.id for country in self.countries]
        if self.summary: 
            data["summary"] = self.summary
        
        if self.themes: 
            data["themes"] = [theme.name for theme in self.themes]      
        
        # if self.childEvents: 
        #     data["childEventIDs"] = [event.id for event in self.childEvents]
        
        # if self.parentEvents: 
        #     data["parentEventIDs"] = [event.id for event in self.parentEvents]
       
        return data



class Theme(db.Model):
    __tablename__ = "theme"
 
    id: so.Mapped[int] = so.mapped_column(primary_key= True), 
    name: so.Mapped[str] = so.mapped_column(sa.String(50), nullable = False)
