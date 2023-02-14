import os
import requests

class BreweryAPI:
    url = os.getenv("url_punk")

    @classmethod
    def get_beers(cls, page: int = None, limit: int = None):
        end_point = 'beers/'
        if page and limit:
            end_point += f'?page={page}&per_page={limit}'
        try:
            response = requests.get(cls.url + end_point, timeout=15).json()
            return response
        except TimeoutError:
            return []
        except Exception as e:
            print(e)
            raise e

    @classmethod
    def get_random(cls):
        end_point = 'beers/random/'
        try:
            response = requests.get(cls.url + end_point, timeout=15).json()
            return response
        except TimeoutError:
            return {}
        except Exception as e:
            print(e)
            raise e

    @classmethod
    def get_by_filter(cls, filters: dict):
        end_point = 'beers/?'
        end_point += ''.join([f'{key}={value}' for key, value in filters.items()])
        try:
            response = requests.get(cls.url + end_point, timeout=15).json()
            return response
        except TimeoutError:
            return []
        except Exception as e:
            print(e)
            raise e