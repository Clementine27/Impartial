from __future__ import annotations
from typing import Optional
from app import db
import sqlalchemy as sa 
import sqlalchemy.orm as so 

association_table = sa.Table(
    "association_table", 
    db.Model.metadata, 
    sa.Column(
        "country_id", sa.ForeignKey("country.id"), primary_key= True 
    ), 
    sa.Column(
        "events_id", sa.ForeignKey("events.id"), primary_key= True 
    ), 
)

# class CountryMixin(object):
#     def to_collection(query, **kwargs): 
        
         

class Country(db.Model): 
    __tablename__ = "country"
    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    country: so.Mapped[str] = so.mapped_column(sa.String, unique = True, nullable= False)
    continent: so.Mapped[str] = so.mapped_column(sa.String, nullable= False)
    # variations: 
    
    events: so.Mapped[list[Events]] = so.relationship(secondary=association_table, back_populates="countries")

    def __repr__(self):
        return super().__repr__()
    
    def to_dict(self): 
        data = {
            "id": self.id, 
            "name": self.country, 
            "continent": self.continent
        }
        return data 
    
    
    
    
class Events(db.Model): 
    __tablename__ = "events"

    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    name: so.Mapped[str] = so.mapped_column(sa.String(50), nullable = False)
    year: so.Mapped[int] = so.mapped_column(sa.Integer, nullable = False)    
    theme: so.Mapped[str] = so.mapped_column(sa.String(50)) 
    summary: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)
    # country_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Country.id), index = True)
    countries: so.Mapped[list[Country]] = so.relationship(secondary=association_table, back_populates="events")
    
        
    def __repr__(self):
        return '<Events {}>'.format(self.body)




