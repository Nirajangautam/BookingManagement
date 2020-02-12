from django import forms
from app.models import User,Venues,Events,Movies,Mbooking,Ebooking

class UserForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields='__all__'

class VenueForm(forms.ModelForm):
	class Meta:
		model=Venues
		fields='__all__'

class EventForm(forms.ModelForm):
	StartDate=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
	EndDate=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
	StartTime=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"time"}))
	EndTime=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"time"}))
	class Meta:
		model=Events
		fields='__all__'

class MovieForm(forms.ModelForm):
	StartDate=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
	EndDate=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"date"}))
	StartTime=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"time"}))
	EndTime=forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type":"time"}))
	class Meta:
		model=Movies
		fields='__all__'		

class Mbookingform(forms.ModelForm):
	class Meta:
		model=Mbooking	
		fields='__all__'
		
class Ebookingform(forms.ModelForm):
	class Meta:
		model=Ebooking
		fields='__all__'			