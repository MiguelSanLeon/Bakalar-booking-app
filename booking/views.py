from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from .forms import EditProfileForm
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
