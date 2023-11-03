from django.urls import path
from . import views
from .views import HomePage, MenuPage, LocationPage, BookingPage, EditPage


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('menu/', views.MenuPage.as_view(), name="menu"),
    path('edit/', views.EditPage.as_view(), name="edit"),
    path('location/', views.LocationPage.as_view(), name="location"),
    path('booking/', views.BookingPage.as_view(), name="booking"),
    path('confirm_booking/<uuid:booking_id>/',
         views.confirm_booking, name='confirm_booking'),
    path('save_booking/<uuid:booking_id>/',
         views.save_booking, name='save_booking'),
]
