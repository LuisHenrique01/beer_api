from chalice import Chalice

app = Chalice(app_name='api_cervejas')


@app.route('/beers')
def index():
    return 


# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

@app.on_sns_message()