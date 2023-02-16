from chalicelib.database.models import Brewery
from chalicelib.network.punkapi import BreweryAPI

def get_beers(page: int = None, limit: int = None):
    db_qtd_beers = Brewery.count_documents()
    if (page and limit) and db_qtd_beers >= (page * limit):
        return list(Brewery.filter({}, page=page, limit=limit))
    response = BreweryAPI.get_beers(page=page, limit=limit)
    Brewery.save_many(response)
    return response


def filter_beers(filters: dict):
    db_response = list(Brewery.filter(filters))
    if db_response:
        return db_response
    response = BreweryAPI.get_beers(filters)
    Brewery.save_many(response)
    return response