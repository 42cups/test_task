# Create your views here.
from django.views.generic import  ListView
from models import *
#from forms import ShowBioForm

class ShowBio(ListView):

	model = Person
	context_object_name = 'person'
	template_name = 'main.html'

class ShowRequests(ListView):

	model = RequestDB
	def get_context_data(self, **kwargs):
		context = super(ShowRequests, self).get_context_data(**kwargs)
		try:
			context['object'] = self.model.objects.all().order_by('-date')[:10]
		except IndexError:
			context['object'] = self.model.objects.all()
		return context

	template_name = 'last_10.html'