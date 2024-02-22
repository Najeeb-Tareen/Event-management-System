from django import forms
from .models import Person, Registration, Event, Team


class Person_form(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['f_name', 'email', 'password']

class Reg_Form(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    class Meta:      
        model = Registration
        fields = '__all__'

class Team_form(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


