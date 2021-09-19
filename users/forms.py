from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# inherit from usercreationform
class UserRegisterForm(UserCreationForm):

    class Meta:
        # specifly model to interact with. whenever this validiates it will create new user
        model = User
        fields = ['username', 'password1', 'password2']