from . import views
from django.urls import path
from .views import HomePage, MenuPage, LocationPage, BookingPage, EditPage


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('menu/', views.MenuPage.as_view(), name="menu"),
    path('edit/', views.EditPage.as_view(), name="edit"),
    path('location/', views.LocationPage.as_view(), name="location"),
    path('booking/', views.BookingPage.as_view(), name="booking"),
]
