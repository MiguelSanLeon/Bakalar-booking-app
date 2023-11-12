from django.shortcuts import render, reverse, redirect, get_object_or_404
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
            return HttpResponseRedirect(reverse('preview_booking', kwargs={'form': form}))
        else:
            print(form.errors)
            return render(request, "booking.html", {'form': form})


class PreviewBookingPage(View):
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            return render(request, 'confirmation.html', {'form': form})
        else:
            return render(request, "booking.html", {'form': form})


class BookingSaved(View):
    template_name = 'new-booking.html'

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = 0 
            booking.save()
            return render(request, self.template_name, {'booking': booking})
        else:
            return render(request, "booking.html", {'form': form})


def check_bookings(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, 'check-bookings.html', {'bookings': user_bookings})
    else:
        return render(request, 'login.html')


class EditBookingPage(View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        form = BookingForm(instance=booking)
        return render(request, "edit-booking.html", {'form': form})

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated')
            return HttpResponseRedirect(reverse('check_bookings'))
        return render(request, "edit-booking.html", {'form': form})


def confirm_delete(request, booking_id):
    return render(request, 'confirm-delete.html', {'booking_id': booking_id})


def delete_booking(request, booking_id):
    if request.method == 'POST' and request.POST.get('confirm_delete') == 'true':
        booking = get_object_or_404(Booking, booking_id=booking_id)
        booking.delete()
        return redirect('check_bookings')
    return redirect('home')


def form_errors(request, form):
    errors = {field: form.errors[field] for field in form.errors}
    return render(request, 'form_errors.html', {'errors': errors})
