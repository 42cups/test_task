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