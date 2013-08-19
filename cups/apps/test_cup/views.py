# Create your views here.
from django.views.generic import  ListView
from models import *
from forms import ShowBioForm

class ShowBio(ListView):

	model = Person
	context_object_name = 'person'
	template_name = 'main.html'