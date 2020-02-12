from django.shortcuts import render,redirect
from app.models import Venues
from app.forms import VenueForm
from django.http import HttpResponse,JsonResponse

def Venue(request):
	venues=Venues.objects.all()
	return render(request,"Venue/venues.html",{'venues':venues})

def Venues_Create(request):
	if request.method=="POST":
		venueforms=VenueForm(request.POST,request.FILES)
		venueforms.save()
		return redirect("/venues")
	venueforms=VenueForm()
	return render(request,"Venue/venuesform.html",{'venueforms':venueforms})

def Edit_Venues(request,id):
	venue=Venues.objects.get(S_No=id)
	return render(request,"Venue/venueEdit.html",{'venue':venue})

def Update_Venues(request,id):
	venue=Venues.objects.get(S_No=id)
	venueforms=VenueForm(request.POST,request.FILES,instance=venue)
	venueforms.save()
	return redirect("/venues")

def Delete_Venues(request,id):
	venue=Venues.objects.get(S_No=id).Venue_img.delete(save=False)
	venue=Venues.objects.get(S_No=id)
	venue.delete()
	return redirect("/venues")	

def Venues_Search(request):
	venues=Venues.objects.filter(Venue_Name__icontains=request.GET['search']).values()
	return JsonResponse(list(venues),safe=False)