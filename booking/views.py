from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect, HttpResponseForbidden
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


class EditUserPage(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = EditProfileForm(instance=user_profile)
        return render(request, "edit-user.html", {"form": form})

    def post(self, request, *args, **kwargs):
        user_profile = request.user.user_profile
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            user = request.user
            user.first_name = user_profile.first_name
            user.last_name = user_profile.last_name
            user.save()

            messages.success(
                request, 'Your profile has been updated successfully!')

            return HttpResponseRedirect(reverse('home'))
        return render(request, "edit-user.html", {'form': form})


class BookingPage(View):
    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(request, "booking.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(
                reverse('preview_booking', kwargs={'form': form}))
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

            messages.success(
                request, 'Your Booking has been saved!')

            return render(request, self.template_name, {'booking': booking})
        else:
            print(form.errors)
            return render(request, "booking.html", {'form': form})


def check_bookings(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        return render(
            request, 'check-bookings.html', {'bookings': user_bookings})
    else:
        return render(request, 'login.html')


class EditBookingPage(View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        if request.user != booking.user:
            return self.forbidden_response(request)

        form = BookingForm(instance=booking)
        return render(request, "edit-booking.html", {'form': form})

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 0
            booking.save()

            messages.success(request, 'Your booking has been updated')

            return HttpResponseRedirect(reverse('check_bookings'))
        print(form.errors)
        return render(request, "edit-booking.html", {'form': form})

    def forbidden_response(self, request):
        return render(
            request,
            'forbidden-page.html',
            {'message': "You don't have permission to access this booking."},
            status=403
        )


def confirm_delete(request, booking_id):
    return render(request, 'confirm-delete.html', {'booking_id': booking_id})


def delete_booking(request, booking_id):
    if (
        request.method == 'POST' and
        request.POST.get('confirm_delete') == 'true'
    ):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        booking.delete()

        messages.success(
            request, 'Your Booking has been deleted!')

        return redirect('check_bookings')
    return redirect('home')


def form_errors(request, form):
    errors = {field: form.errors[field] for field in form.errors}
    return render(request, 'form_errors.html', {'errors': errors})
