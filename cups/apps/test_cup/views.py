# Create your views here.
from django.views.generic import  ListView,UpdateView,TemplateView,DetailView
from models import *
from forms import ShowBioForm
import json
from django.http import HttpResponse


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

class UpdateBio(DetailView):

    model = Person
    template_name = 'change.html'
    form_class = ShowBioForm
    # success_url = '#'
    context_object_name = 'person'


def ajax(request):
    if request.is_ajax() :
        form = ShowBioForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            pk = request.POST['pk']
            p = Person.objects.filter(pk=pk)
            print('------------------OK FORM------------------'+'\n',data)
            f = ShowBioForm(request.POST,instance=p[0])
            f.save()

            return HttpResponse('ok')
        else :
            print('------------------ERROR------------------'+'\n',form.cleaned_data)
            return HttpResponse('______________NOT VALID_____________')
    else :
        return HttpResponse('______________NOT AJAX_____________')