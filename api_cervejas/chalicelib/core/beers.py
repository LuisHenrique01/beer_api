import os
from chalicelib.database.models import Brewery
from chalicelib.network.punkapi import BreweryAPI

def get_beers(page: int = None, limit: int = None):
    
    beers = Brewery.filter({}, page=page, limit=limit)
