from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def home(request):
    return render(request, 'auth_user/home.html')

