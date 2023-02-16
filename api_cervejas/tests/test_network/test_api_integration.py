import unittest
import requests_mock

from chalicelib.network.punkapi import BreweryAPI


class TestBreweryAPI(unittest.TestCase):
    @requests_mock.Mocker()
    def test_get_beers(self, m):
        url = 'http://test.com/beers/'
        m.get(url, json={'data': []})
        beers = BreweryAPI.get_beers()
        self.assertEqual(beers, {'data': []})

        page = 1
        limit = 10
        url += f'?page={page}&per_page={limit}'
        m.get(url, json={'data': []})
        beers = BreweryAPI.get_beers(page=page, limit=limit)
        self.assertEqual(beers, {'data': []})

    @requests_mock.Mocker()
    def test_get_random(self, m):
        url = 'http://test.com/beers/random/'
        m.get(url, json={})
        beer = BreweryAPI.get_random()
        self.assertEqual(beer, {})

    @requests_mock.Mocker()
    def test_get_by_filter(self, m):
        url = 'http://test.com/beers/?'
        filter_params = {'foo': 'bar', 'baz': 'qux'}
        url += ''.join([f'{key}={value}' for key, value in filter_params.items()])
        m.get(url, json={'data': []})
        beers = BreweryAPI.get_by_filter(filter_params)
        self.assertEqual(beers, {'data': []})