from django.test import TestCase
from surfers.models import Surfer, Shaper, Surfboard
import requests

api_url = "http://localhost:8000/api/"

class BaseAPITestCase(TestCase):
    def test_get_post(self):
        json_header = {"Accept": "application/json"}
        html_header = {"Accept": "text/html"}
        response = requests.get(api_url, headers=json_header)
        self.assertTrue("application/json" in response.headers["Content-Type"].lower())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"version": "1.0", "method": "get"})
        response = requests.get(api_url, headers=html_header)
        self.assertTrue("text/html" in response.headers["Content-Type"].lower())
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<html>" in response.text.lower())

        response = requests.post(api_url, headers=json_header)
        self.assertTrue("application/json" in response.headers["Content-Type"].lower())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"version": "1.0", "method": "post"})
        response = requests.post(api_url, headers=html_header)
        self.assertTrue("text/html" in response.headers["Content-Type"].lower())
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<html>" in response.text.lower())


class SurferAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_change_name_skill(self):
        self.assertEqual(Surfer.objects.count(), 0)


class ShaperAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_change_name_year(self):
        self.assertEqual(Shaper.objects.count(), 0)


class SurfboardAPITestCase(TestCase):
    def test_change_name_owner(self):
        self.assertEqual(Surfboard.objects.count(), 0)
