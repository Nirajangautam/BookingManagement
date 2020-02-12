from django.shortcuts import render,redirect
from app.models import Movies
from app.forms import MovieForm
from django.http import HttpResponse,JsonResponse

def Movie(request):
	mov=Movies.objects.all()
	return render(request,"Movies/movies.html",{'mov':mov})	

def Movies_Create(request):
	if request.method=="POST":
		movieform=MovieForm(request.POST,request.FILES)
		movieform.save()
		return redirect("/movies")
	movieform=MovieForm()
	return render(request,"Movies/Moviesform.html",{'mov':movieform})
    
def Edit_movies(request,id):
	mov=Movies.objects.get(movie_id=id)
	return render(request,"Movies/Moviesedit.html",{'mov':mov})

def Update_movies(request,id):
	mov=Movies.objects.get(movie_id=id)
	movieform=MovieForm(request.POST,request.FILES,instance=mov)
	movieform.save()
	return redirect("/movies")

def Delete_movies(request,id):
	mov=Movies.objects.get(movie_id=id).Poster.delete(save=False)
	mov=Movies.objects.get(movie_id=id)
	mov.delete()
	return redirect("/movies")	

def Movie_Search(request):
	movie=Movies.objects.filter(movie_Name__icontains=request.GET['search']).values()
	return JsonResponse(list(movie),safe=False)		