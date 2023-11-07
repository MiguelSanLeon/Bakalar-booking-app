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
    path('check-bookings/', views.check_bookings, name='check_bookings'),
    path('edit-booking/<uuid:booking_id>/',
         views.EditBookingPage.as_view(), name='edit_booking'),
    path('confirm-delete/<uuid:booking_id>/',
         views.confirm_delete, name='confirm_delete'),
    path('delete-booking/<uuid:booking_id>/',
         views.delete_booking, name='delete_booking'),
]
