from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile, Booking
from django.core.validators import RegexValidator
from datetime import datetime, timedelta


# Custom signup form extending the default SignupForm from allauth
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    phone_number = forms.CharField(
        max_length=11,
        label='Phone Number',
        validators=[RegexValidator(
            r'^\d{11}$', 'Enter a valid 11-digit phone number.')]
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        phone_number = self.cleaned_data['phone_number']

        try:
            user_profile = UserProfile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number)
            user_profile.save()
        except Exception as e:
            print(f"Error creating user profile: {e}")

        return user


# Form for editing user profile
class EditProfileForm(forms.ModelForm):

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number'}),
        validators=[RegexValidator(
            r'^\d{11}$', 'Enter a valid 11-digit phone number.')]
    )

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number')


# Form for creating or editing a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time',
                  'booking_comments', 'guest_num']
        widgets = {
            'booking_date': forms.DateInput(
                attrs={'type': 'date', 'required': True}),
            'booking_time': forms.TimeInput(
                attrs={'type': 'time', 'required': True}),
            'booking_comments': forms.Textarea(
                attrs={'required': False}),
            'guest_num': forms.NumberInput(
                attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        instance = self.instance

        if self.instance:
            self.fields['booking_date'].initial = instance.booking_date
            self.fields['booking_time'].initial = instance.booking_time
            self.fields['booking_comments'].initial = instance.booking_comments
            self.fields['guest_num'].initial = instance.guest_num

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date:
            today = datetime.now().date()
            if booking_date < today:
                raise forms.ValidationError(
                    "Invalid date. Please select a date in the future.")
        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        if booking_time:
            min_time = datetime.strptime('14:00', '%H:%M').time()
            max_time = datetime.strptime('22:00', '%H:%M').time()
            if not min_time <= booking_time <= max_time:
                raise forms.ValidationError(
                    "Invalid time. Please select a time between"
                    "14:00 and 22:00.")
        return booking_time

    def clean_guest_num(self):
        guest_num = self.cleaned_data.get('guest_num')
        if guest_num and guest_num > 12:
            raise forms.ValidationError(
                "In case you need to book for more than 12 people, please"
                "contact us on our phone number 55 555 345 2126.")
        return guest_num
