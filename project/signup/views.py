from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserInfoForm

# Create your views here.

def FillUserForm(request):
	if request.method == "POST":
		form = UserInfoForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			email = form.cleaned_data.get('email')
			cabinet = form.cleaned_data.get('cabinet')
			password = form.cleaned_data.get('password')
			if first_name and last_name and email and cabinet and password:
				user = UserInfo.objects.create(first_name=first_name, last_name=last_name, email=email, cabinet=cabinet, password=password)
				user.save()
		return redirect('home')
	else:
		form = UserInfoForm()
	return render(request, 'signup.html', {'form': form})