from django import forms
from .models import City, ContactModel


class CitySelectionForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), initial=City.objects.get(id=1))


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))


    class Meta:
        model = ContactModel
        fields = '__all__'
