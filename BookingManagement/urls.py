"""BookingManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import Userviews,Eventviews,Venueviews,Movieviews,Ebooking,Mbooking,home
urlpatterns = [
    path('mypage',Userviews.mypage),
    path('users',Userviews.Users),
    path('entry',Userviews.entry),
    path('edit/<int:id>',Userviews.Edit_Users),
    path('update/<int:id>',Userviews.Update_Users),
    path('delete/<int:id>',Userviews.Delete_Users),
    path('form',Userviews.Userform_Create),
    path('search',Userviews.Users_Search),
    #venue
    path('venues',Venueviews.Venue),
    path('venueform',Venueviews.Venues_Create),
    path('searchvenues',Venueviews.Venues_Search),
    path('deletevenue/<int:id>',Venueviews.Delete_Venues),
    path('updatevenue/<int:id>',Venueviews.Update_Venues),
    path('editvenue/<int:id>',Venueviews.Edit_Venues),
    #Events
    path('deleteevent/<int:id>',Eventviews.Delete_Event),
    path('editevent/<int:id>',Eventviews.Edit_Event),
    path('updateevent/<int:id>',Eventviews.Update_Event),
    path('eventform',Eventviews.Events_Create),
    path('events',Eventviews.Event),
    path('eventsearch',Eventviews.Event_Search),
    #movies
    path('editmovies/<int:id>',Movieviews.Edit_movies),
    path('deletemovies/<int:id>',Movieviews.Delete_movies),
    path('updatemovies/<int:id>',Movieviews.Update_movies),
    path('movieform',Movieviews.Movies_Create),
    path('movies',Movieviews.Movie),
    path('searchmov',Movieviews.Movie_Search),
    #login
    path('login',Userviews.login),
    #EventBooking
    path('ebook',Ebooking.EventBooking),
    path('ebookform',Ebooking.Ebook_Create),
    path('editEbook/<int:id>',Ebooking.Edit_Ebook),
    path('deleteEbook/<int:id>',Ebooking.Delete_Ebook),
    path('UpdateEbook/<int:id>',Ebooking.Update_Ebook),
    path('Esearch',Ebooking.Ebook_Search),
    #MovieBooking
    path('mbook',Mbooking.MovieBooking),
    path('mbookform',Mbooking.Mbook_Create),
    path('editmbook/<int:id>',Mbooking.Edit_Mbook),
    path('deletembook/<int:id>',Mbooking.Delete_Mbook),
    path('Updatembook/<int:id>',Mbooking.Update_Mbook),
    #home
    path('home',home.Home)



    ]
