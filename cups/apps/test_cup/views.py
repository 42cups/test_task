from django.views.generic import  ListView
from models import *

class ShowBio(ListView):

        model = Person
        context_object_name = 'person'
        template_name = 'main.html'
