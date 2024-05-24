
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/user')
def home(request):
    # if request.user.is_superuser:
    return render(request,'landload/index.html',{'user':request.user})
