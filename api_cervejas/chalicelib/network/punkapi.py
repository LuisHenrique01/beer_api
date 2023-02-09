import os
import requests

class BreweryAPI:

    def __init__(self) -> None:
        self.url = os.getenv("url_punk")

    def get_beers(self):
        try:
            end_point = 'beers/'
            return requests.get(self.url + end_point, timeout=15).json()
        except TimeoutError:
            return []
        except Exception as e:
            print(e)
            raise e
        
    def get_random(self):
        try:
            end_point = 'beers/random/'
            return requests.get(self.url + end_point, timeout=15).json()
        except TimeoutError:
            return {}
        except Exception as e:
            print(e)
            raise e
        
    def get_by_filter(self, filters: dict):
        try:
            end_point = 'beers/?'
            end_point += ''.join([f'{key}={value}' for key, value in filters.items()])
            return requests.get(self.url + end_point, timeout=15).json()
        except TimeoutError:
            return []
        except Exception as e:
            print(e)
            raise e
