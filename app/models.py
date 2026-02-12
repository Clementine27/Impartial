from __future__ import annotations
from typing import Optional
from app import db
import sqlalchemy as sa 
import sqlalchemy.orm as so 
import json 

association_table = sa.Table(
    "association_table", 
    db.Model.metadata, 
    sa.Column(
        "country_id", sa.ForeignKey("country.id", name = "countryIDKey"), primary_key= True ), 
    sa.Column(
        "events_id", sa.ForeignKey("events.id", name = "eventIDKey"), primary_key= True )
)

# given a collection object, 
class ObjectToDictMixin: 
    def toDict(objects): 
        objList = []
        for obj in objects: 
            jsonObj = json.dumps(vars(obj))
            objList.append(jsonObj)
        return objList
         

class Country(ObjectToDictMixin, db.Model): 
    __tablename__ = "country"
    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    country: so.Mapped[str] = so.mapped_column(sa.String, unique = True, nullable= False)
    continent: so.Mapped[str] = so.mapped_column(sa.String, nullable= False)
    # variations: 
    
    events: so.Mapped[list[Events]] = so.relationship(secondary=association_table, back_populates="countries")

    def __repr__(self):
        return '<Country {}>'.format(self.country)
    
        
    def to_dict(self): 
        data = {
            "id": self.id, 
            "name": self.country, 
            "continent": self.continent, 
            "events": dict(self.events.to_dict())
        }
        return data 
    
class Events(db.Model): 
    __tablename__ = "events"

    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    name: so.Mapped[str] = so.mapped_column(sa.String(50), nullable = False)
    startYear: so.Mapped[int] = so.mapped_column(sa.Integer, nullable = False)  
    endYear: so.Mapped[int] = so.mapped_column(sa.Integer)    
    theme: so.Mapped[str] = so.mapped_column(sa.String(50)) 
    summary: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)
    countries: so.Mapped[list[Country]] = so.relationship(secondary=association_table, back_populates="events")
    
    childEvents: so.Mapped[Optional[list[Events]]] = so.relationship("Events", back_populates="parentEvents", remote_side = "events.parentId")
    
    parentId: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey("events.id", name = "parentIDName"))
    parentEvents: so.Mapped[Optional["Events"]] = so.relationship("Events", back_populates= "childEvents", remote_side= "events.id")
        
    def __repr__(self):
        return '<Events {}>'.format(self.name)
    
    def to_dict(self): 
        data = {
            "name": self.name, 
            "startYear": self.startYear, 
            "endYear": self.endYear, 
            "countries": self.countries, 
            "theme": self.theme
        } 
       
        if self.summary: 
            data.summary = self.summary
        if self.childEvents: 
            data.childEvents = self.childEvents
        
        return data



