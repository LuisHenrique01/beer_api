from chalice import Chalice

from chalicelib.core.beers import get_beers, filter_beers

app = Chalice(app_name='api_cervejas')


@app.route('/beers', methods=['GET'])
def get_all():
    params = app.current_request.query_params or {}
    return get_beers(params)


@app.route('/beers-filter', methods=['GET'])
def filter():
    params = app.current_request.query_params or {}
    return filter_beers(params)