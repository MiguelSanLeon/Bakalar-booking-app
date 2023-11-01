from . import views
from django.urls import path
from .views import HomePage, MenuPage


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('menu/', views.MenuPage.as_view(), name="menu"),
]
