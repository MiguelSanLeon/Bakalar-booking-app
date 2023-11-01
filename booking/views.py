from django.shortcuts import render
from django.views import generic, View
from .models import Booking


class HomePage(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class MenuPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")
