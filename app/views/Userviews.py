from django.shortcuts import render,redirect
from app.models import User,Movies,Venues,Events
from app.forms import UserForm,VenueForm,EventForm
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate


@Authenticate.valid_user
def Users(request):
	limit=3
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "back" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		users=User.objects.raw("select * from User limit 3 offset %s",[offset])
	else:
		users=User.objects.raw("select * from User limit 3 offset 0")
	return render(request,"User/Users.html",{'users':users,'page':page})


def login(request):
	return render(request,"login.html")

def entry(request):
	request.session['Email']=request.POST['Email']
	users=User.objects.get(Email=request.POST['Email'])
	venues=Venues.objects.all()
	mov=Movies.objects.all()
	event=Events.objects.all()
	request.session['Username']=users.Username
	return render(request,'homepage.html',{'users':users,'mov':mov,'event':event,'venues':venues})	
	

def mypage(request):
	return render(request,'homepage.html')




def Userform_Create(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect("/users")
	form=UserForm()
	return render(request,"User/Userform.html",{'form':form})

def Edit_Users(request,id):
	user=User.objects.get(user_id=id)
	return render(request,"User/Edit.html",{'user':user})

def Update_Users(request,id):
	user=User.objects.get(user_id=id)
	form=UserForm(request.POST,request.FILES,instance=user)
	form.save()
	return redirect("/users")

def Delete_Users(request,id):
	if Profile_Pic!='defaultimg.png':
		user=User.objects.get(user_id=id).Profile_Pic.delete(save=False)
	
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect("/users")

def Users_Search(request):
	users=User.objects.filter(Username__icontains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)
