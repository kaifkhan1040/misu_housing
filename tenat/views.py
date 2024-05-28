
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import CustomUser
from users.forms import UserProfileForm

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
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_success')  # Redirect to a success page
        else:
            print("error",forms.error)
    else:
        form = UserProfileForm(instance=user)
    return render(request,'tenat/page-account-settings-account.html',{'form':form,'user':request.user})
