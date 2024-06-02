
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import CustomUser
from users.forms import UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/user')
def home(request):
    # if request.user.is_superuser:
    return render(request,'tenat/index.html',{'user':request.user})

@login_required(login_url='/user')
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        print("after post,,,,,,,,,,,,,,,,")
        form = UserProfileForm(request.POST, request.FILES,instance=user)
        print('%'*100)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('tenat:profile')  # Redirect to a success page
        else:
            print("error",forms.error)
    else:
        form = UserProfileForm(instance=user)
    return render(request,'tenat/page-account-settings-account.html',{'form':form,'user':request.user})

@login_required(login_url='/user')
def deactivate(request):
    print('start')
    if request.method == 'POST':
        print('after post')

        status = request.POST.get('accountActivation',None)
        if status!= None:
            obj=CustomUser.objects.get(id=request.user.id)
            obj.is_active=False
            obj.save()
            # logout(request)
            messages.success(request,'You account deactivate successfully')
            # return HttpResponseRedirect(reverse_lazy('user:login'))
            return JsonResponse(True,safe=False)
    return redirect('tenat:profile')
    
