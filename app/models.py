from django.db import models
from django import forms

class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	Username=models.CharField(max_length=30)
	Password=models.CharField(max_length=20)
	Email=models.CharField(max_length=40)
	Contact_Number=models.CharField(max_length=50)
	Profile_Pic=models.ImageField(default="defaultimg.png",upload_to="images/")
	class Meta:
		db_table="user"

class Venues(models.Model):
	S_No=models.AutoField(auto_created=True,primary_key=True)
	Venue_Name=models.CharField(max_length=30)
	Venue_img=models.ImageField(upload_to="images/")
	class Meta:
		db_table="venues"	

class Events(models.Model):
	event_id=models.AutoField(auto_created=True,primary_key=True)
	StartDate=models.DateField() 
	EndDate=models.DateField() 
	StartTime=models.TimeField()
	EndTime=models.TimeField() 
	Event_Name=models.CharField(max_length=40)
	Events_Details=models.CharField(max_length=1000)
	Casts=models.CharField(max_length=100)
	Poster=models.ImageField()
	Trailer=models.FileField(upload_to="videos/",null=True) 
	class Meta:
		db_table="events"

class Movies(models.Model):
	movie_id=models.AutoField(auto_created=True,primary_key=True)
	movie_Name=models.CharField(max_length=40)
	StartDate=models.DateField() 
	EndDate=models.DateField() 
	StartTime=models.TimeField()
	EndTime=models.TimeField() 
	Movie_Details=models.CharField(max_length=1000)
	Casts=models.CharField(max_length=100)
	Poster=models.ImageField()
	Trailer=models.FileField(upload_to="videos/",null=True) 
	class Meta:
		db_table="movies"
	
class Mbooking(models.Model):
	Mbooking_id=models.AutoField(auto_created=True,primary_key=True)
	Movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
	Bookedby=models.ForeignKey(User,on_delete=models.CASCADE)
	M_Venue=models.ForeignKey(Venues,on_delete=models.CASCADE)
	class Meta:
		db_table="Mbooking"

class Ebooking(models.Model):
	Ebooking_id=models.AutoField(auto_created=True,primary_key=True)
	Event=models.ForeignKey(Events,on_delete=models.CASCADE)
	Bookedby=models.ForeignKey(User,on_delete=models.CASCADE)
	E_Venue=models.ForeignKey(Venues,on_delete=models.CASCADE)
	class Meta:
		db_table="Ebooking"