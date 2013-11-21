from django import forms
from models import Person

class ShowBioForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','type':'text','id':'name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text','id':'last_name'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','id':'birth'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','type':'email','id':'email'}))
    jabber = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','type':'text','id':'jabber'}))
    skype = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text','id':'skype'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text','id':'bio'}))
    other_contacts = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text','id':'other_contacts'}))

    class Meta:
        model = Person
        exclude = ('contacts','photo')
