
from django.shortcuts import render, redirect


def index(request):
    # if request.user.is_authenticated:
    #     return redirect("customadmin:home")
    # if CompanySubscription.objects.filter(id=request.user.id).exists():
    #     return redirect('customadmin:home')
    return render(request,'index.html',{'user':request.user})