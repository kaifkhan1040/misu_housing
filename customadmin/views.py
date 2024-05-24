from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/user')
def home(request):
    return render(request,'customadmin/index.html',{'user':request.user})
