from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        widgets = {
          'first_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'last_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'username': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'password1': forms.PasswordInput(attrs={'class':'form-control mb-3'}),
          'password2': forms.PasswordInput(attrs={'class':'form-control mb-3'}),
          'email': forms.TextInput(attrs={'class':'form-control mb-3'})
      }


class UserUpdateForm(forms.ModelForm):

    class Meta:
      model = User
      fields = ['first_name', 'last_name', 'username', 'email']
      widgets = {
          'first_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'last_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'username': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'email': forms.TextInput(attrs={'class':'form-control mb-3'})
      }

