from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from .forms import EditProfileForm, BookingForm
from .models import Booking, UserProfile


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class MenuPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")


class LocationPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "location.html")


class EditPage(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = EditProfileForm(instance=user_profile)
        return render(request, "edit.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        user_profile = request.user.user_profile
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            user = request.user
            user.first_name = user_profile.first_name
            user.last_name = user_profile.last_name
            user.save()
            return HttpResponseRedirect(reverse('home'))
        return render(request, "edit.html", {'form': form})


class BookingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "booking.html")
   
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            booking_comments = form.cleaned_data['booking_comments']
            guest_num = form.cleaned_data['guest_num']

            booking = Booking(
                user=request.user,
                booking_date=booking_date,
                booking_time=booking_time,
                booking_comments=booking_comments,
                guest_num=guest_num,
                status=0
            )
            booking.save()

            return render(request, 'confirmation.html', {'booking': booking})
        else:
            return render(request, "booking.html", {'form': form})
