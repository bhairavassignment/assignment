from django.shortcuts import render, redirect
from first.forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


def register(request):

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			current_site = get_current_site(request)
			mail_subject = 'Account Registration'
			message = 'Registration Successful'
			to_email = request.POST['email']
			email = EmailMessage(
				mail_subject, message, to=[to_email]
			)
			email.send()

			return redirect("/home_success")
		else:
			params = {"form":form}
			return render(request,"registrationform.html",params)

	else:
		form = RegistrationForm()
		params = {"form":form}
		return render(request,"registrationform.html",params)


def home(request):
		return render(request,"home.html")

def home_success(request):
		return render(request,"home_success.html")