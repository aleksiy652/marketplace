from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class Register_form(UserCreationForm):
    class Meta():
        model = Polbzovatelb
        fields = ['username', 'password1', 'password2', 'email', 'address', 'phone']


class Profile_form(UserChangeForm):
    class Meta():
        model = Polbzovatelb
        fields = ['username', 'address', 'phone']
