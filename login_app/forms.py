from django import forms
from landapp.models import land
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class landForm(forms.ModelForm):
    class Meta:
        model = land
        fields = '__all__'  # Include all fields except owner

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.instance.owner = self.user


class SignUpForm(UserCreationForm): 
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
