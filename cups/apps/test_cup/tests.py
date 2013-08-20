from django_webtest import WebTest
from models import *

class TestCase(WebTest):

	fixtures = ['initial_data.json',]
	#info = Person.objects.get(pk=1)

	def test_1t_page(self):
		"""
		tests, that 1 ticket page exists and show correct data
		"""
		resp = self.app.get('/')
		assert resp.status == '200 OK'

	def test_3t_requests_link_exists(self):
		"""
		tests, that main page have link to requests page and it works
		"""
		resp = self.app.get('/')
		next_step = resp.click('requests')
		assert next_step.status == '200 OK'

	def test_3t_request_page_show_requests(self):
		"""
		check, that response list exists
		"""
		resp = self.app.get('/last_10/')
		assert '<ul>' in str(resp.html)

	def test_t4_settings_c_processor(self):
		"""
		test display of custom context processor
		"""
		resp = self.app.get('/last_10/')
		assert '<p>' in str(resp.html)
