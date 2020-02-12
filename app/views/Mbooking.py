from django.shortcuts import render,redirect
from app.models import Mbooking,Venues,User,Movies
from app.forms import Mbookingform
from django.http import HttpResponse,JsonResponse

def MovieBooking(request):
	M_booking=Mbooking.objects.all()
	return render(request,"MovieBooking/Mbooking.html",{'mbook':M_booking})	

def Mbook_Create(request):
	venue=Venues.objects.all()
	user=User.objects.all()
	movie=Movies.objects.all()
	if request.method=="POST":
		Mbookforms=Mbookingform(request.POST)
		Mbookforms.save()
		return redirect("/mbook")
	Mbookforms=Mbookingform()
	return render(request,"MovieBooking/Mbookingform.html",{'mbookform':Mbookforms,'venue':venue,'user':user,'movie':movie})

    
def Edit_Mbook(request,id):
	venue=Venues.objects.all()
	user=User.objects.all()
	movie=Movies.objects.all()

	mbook=Mbooking.objects.get(Mbooking_id=id)
	return render(request,"MovieBooking/Mbookingedit.html",{'mbook':mbook,'venue':venue,'user':user,'movie':movie})

def Update_Mbook(request,id):
	mbook=Mbooking.objects.get(Mbooking_id=id)
	Mbookform=Mbookingform(request.POST,instance=mbook)
	Mbookform.save()
	return redirect("/mbook")

def Delete_Mbook(request,id):
	mbook=Mbooking.objects.get(Mbooking_id=id)
	mbook.delete()
	return redirect("/mbook")		