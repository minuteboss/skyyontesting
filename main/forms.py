from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               'id':'id'
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              'id':'cname'
                                                              }))
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                              'class': 'form-control',
                                                              'id':'uname'
                                                              }))                                                          

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           'id':'register-email-2'
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  
                                                                  'id': 'register-password-2',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  
                                                                  'id': 'register-password-2',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']