from django_webtest import WebTest
from django.core.urlresolvers import reverse
from models import *

class TestCase(WebTest):

    fixtures = ['initial_data.json',]

    def test_1t_page(self):
        """
        tests, that 1 ticket page exists and show correct data
        """
        resp = self.app.get(reverse('main'))
        assert resp.status == '200 OK'

    def test_t3_middleware_m_page(self):
        """
        test that main page has a link to pages with requests
        """
        resp = self.app.get(reverse('main'))
        go_to_requests = resp.click('requests')
        assert go_to_requests.status == '200 OK'

    def test_t3_middleware_req_page_exists(self):
        resp = self.app.get(reverse('requests'))
        assert resp.status == '200 OK'

    def test_t3_middleware_req_exists_on_its_page(self):
        resp = self.app.get(reverse('requests'))
        assert resp.mustcontain('<li>')