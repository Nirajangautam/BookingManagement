from django.shortcuts import render,redirect
from app.models import Ebooking,Venues,User,Events
from app.forms import Ebookingform
from django.http import HttpResponse,JsonResponse

def EventBooking(request):
	E_booking=Ebooking.objects.all()
	return render(request,"EventBooking/Ebooking.html",{'ebook':E_booking})	

def Ebook_Create(request):
	venue=Venues.objects.all()
	user=User.objects.all()
	event=Events.objects.all()
	if request.method=="POST":
		Ebookforms=Ebookingform(request.POST)
		Ebookforms.save()
		return redirect("/ebook")
	Ebookforms=Ebookingform()
	return render(request,"EventBooking/Ebookingform.html",{'ebookform':Ebookforms,'venue':venue,'user':user,'event':event})

    
def Edit_Ebook(request,id):
	venue=Venues.objects.all()
	user=User.objects.all()
	event=Events.objects.all()

	ebook=Ebooking.objects.get(Ebooking_id=id)
	return render(request,"EventBooking/Ebookingedit.html",{'ebook':ebook,'venue':venue,'user':user,'event':event})

def Update_Ebook(request,id):
	ebook=Ebooking.objects.get(Ebooking_id=id)
	Ebookform=Ebookingform(request.POST,instance=ebook)
	Ebookform.save()
	return redirect("/ebook")

def Delete_Ebook(request,id):
	ebook=Ebooking.objects.get(Ebooking_id=id)
	ebook.delete()
	return redirect("/ebook")	

def Ebook_Search(request):
	venue=Venues.objects.all()
	user=User.objects.all()
	event=Events.objects.all()
	ebook=Ebooking.objects.filter(Event_Name__icontains=request.GET['search']).values()
	return JsonResponse(list(ebook),safe=False)		