from chalicelib.database.models import Brewery
from chalicelib.network.punkapi import BreweryAPI

def get_beers(page: int = None, limit: int = None):
    db_qtd_beers = Brewery.count_documents()
    if db_qtd_beers >= (page * limit):
        return list(Brewery.filter({}, page=page, limit=limit))
    response = BreweryAPI.get_beers(page=page, limit=limit)
    # SNS ou SQS para salvar
    return response


