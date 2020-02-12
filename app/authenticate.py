from django.shortcuts import redirect
from app.models import User
from django.contrib import messages

class Authenticate:
	def valid_user(function):
		def wrap(request):
			
			try:
				user.objects.get(email=request.session['email'])
				return function(request)
			except:
				messages.warning(request,"Please enter the valid email/Password")
				return redirect("mypage")
			return wrap