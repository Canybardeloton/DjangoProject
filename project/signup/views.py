from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserInfoForm

# Create your views here.

def FillUserForm(request):
	if request.method == "POST":
		form = UserInfoForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data['user']
			if data:
				user = UserInfo.objects.create(user=data)
				user.save()
		return redirect('home')
	else:
		form = UserInfoForm()
	return render(request, 'signup.html', {'form': form})