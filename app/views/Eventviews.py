from django.shortcuts import render,redirect
from app.models import Events
from app.forms import EventForm
from django.http import HttpResponse,JsonResponse

def Event(request):
	event=Events.objects.all()
	return render(request,"Events/Events.html",{'event':event})	

def Events_Create(request):
	if request.method=="POST":
		eventform=EventForm(request.POST,request.FILES)
		eventform.save()
		return redirect("/events")
	eventform=EventForm()
	return render(request,"Events/EventForm.html",{'event':eventform})
    
def Edit_Event(request,id):
	event=Events.objects.get(event_id=id)
	return render(request,"Events/eventEdit.html",{'event':event})

def Update_Event(request,id):
	event=Events.objects.get(event_id=id)
	eventform=EventForm(request.POST,request.FILES,instance=event)
	eventform.save()
	return redirect("/events")

def Delete_Event(request,id):
	event=Events.objects.get(event_id=id).Poster.delete(save=False)
	event=Events.objects.get(event_id=id)
	event.delete()
	return redirect("/events")	

def Event_Search(request):
	event=Events.objects.filter(Event_Name__icontains=request.GET['search']).values()
	return JsonResponse(list(event),safe=False)	