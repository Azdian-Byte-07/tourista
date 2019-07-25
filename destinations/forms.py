from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'






    '''
         #widgets={"":""}

 class RegistrationForm(forms.ModelForm):
     class Meta:
         model = User
         fields = [ 'email', 'password', 'first_name', 'last_name']

         widgets = {
             'password': forms.PasswordInput(),

         }


 class LoginForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['email', 'password']

         widgets = {
             'password': forms.PasswordInput(),

         }

 '''