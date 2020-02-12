from django.shortcuts import render,redirect
from app.models import Movies,Venues,Events
from app.forms import MovieForm
from app.forms import VenueForm
from django.http import HttpResponse,JsonResponse

def Home(request):
	venues=Venues.objects.all()
	mov=Movies.objects.all()
	event=Events.objects.all()
	return render(request,"homepage.html",{'mov':mov,'venues':venues,'event':event})