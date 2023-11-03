from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from .forms import EditProfileForm, BookingForm
from .models import Booking, UserProfile
from django.contrib import messages


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
        form = BookingForm()
        return render(request, "booking.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = 0
            booking.save()
            return redirect('confirm_booking', booking_id=booking.booking_id)
        else:
            print(form.errors)
            return render(request, "booking.html", {'form': form})



def confirm_booking(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    return render(request, 'confirmation.html', {'booking': booking})


def save_booking(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    booking.save()

    messages.success(request, 'Your booking has been saved in the system')

    return redirect('home')
