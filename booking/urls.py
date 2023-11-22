from django.urls import path
from . import views
from .views import (
    HomePage,
    MenuPage,
    LocationPage,
    BookingPage,
    EditUserPage,
    PreviewBookingPage,
    BookingSaved)


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('menu/', views.MenuPage.as_view(), name="menu"),
    path('edit-user/', views.EditUserPage.as_view(), name="edit_user"),
    path('location/', views.LocationPage.as_view(), name="location"),
    path('booking/', views.BookingPage.as_view(), name="booking"),
    path('check-bookings/', views.check_bookings, name='check_bookings'),
    path('booking-saved/', BookingSaved.as_view(), name='booking_saved'),
    path('edit-booking/<uuid:booking_id>/',
         views.EditBookingPage.as_view(), name='edit_booking'),
    path('preview-booking/', views.PreviewBookingPage.as_view(),
         name='preview_booking'),
    path('confirm-delete/<uuid:booking_id>/',
         views.confirm_delete, name='confirm_delete'),
    path('delete-booking/<uuid:booking_id>/',
         views.delete_booking, name='delete_booking'),
]
