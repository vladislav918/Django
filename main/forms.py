from django import forms
from .models import City, ContactModel


class CitySelectionForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        to_field_name = 'name',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'style': 'width: 100%; height: 150px;'}),
        label='Сообщение'
    )


    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']
