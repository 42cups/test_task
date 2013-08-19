from django import forms
from models import Person

class ShowBioForm(forms.ModelForm):

	class Meta:
		model = Person
		fields =['name','surname','biography','contacts',]
