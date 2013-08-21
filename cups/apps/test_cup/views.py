# Create your views here.
from django.views.generic import  ListView,UpdateView,TemplateView
from models import *
from forms import ShowBioForm

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

class ShowSettings(TemplateView):
    template_name = 'settings.html'

class UpdateBio(UpdateView):

    model = Person
    template_name ='person'
    template_name = 'change.html'
    form_class = ShowBioForm
    success_url = '/'

