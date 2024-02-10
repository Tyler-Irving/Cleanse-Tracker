from django import forms
from django.contrib.auth.models import User
from .models import Cleanse, Restriction


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=150)


class CleanseCreationForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.TextInput()
    start_date = forms.DateField()
    end_date = forms.DateField()


class RestrictionCreationForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)


# fix user, cleanse, restriction fields. Right idea just wrong execution
class CleanseEntryCreationForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    cleanse = forms.ModelChoiceField(queryset=Cleanse.objects.all())
    restriction = forms.ModelChoiceField(queryset=Restriction.objects.all())
    is_completed = forms.BooleanField()
