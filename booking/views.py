from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class MenuPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")
