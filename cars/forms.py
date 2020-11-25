#from django import forms
from django import forms
from cars.models import UserDetails
from django.contrib.auth.forms import UserCreationForm

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
