# forms.py

from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    phone_number = forms.CharField(max_length=11, label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        phone_number = self.cleaned_data['phone_number']
        user_profile = UserProfile.objects.create(
            user=user, first_name=first_name, last_name=last_name, phone_number=phone_number)
        user_profile.save()
        return user
