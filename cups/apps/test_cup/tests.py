from django_webtest import WebTest
from models import *

class TestCase(WebTest):

    fixtures = ['initial_data.json',]

    def test_1t_page(self):
        """
        tests, that 1 ticket page exists and show correct data
        """
        resp = self.app.get('/')
        assert resp.status == '200 OK'
