
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import CustomUser
from django.http import JsonResponse
from django.core.serializers import serialize
from users.email import account_activation_mail,account_rejected_mail
from .forms import EmailTemplateForm
from .models import EmailTemplate
# Create your views here.
@login_required(login_url='/user')
def home(request):
    # if request.user.is_superuser:
    return render(request,'landload/index.html',{'user':request.user})

@login_required(login_url='/user')
def landload_list(request):
    obj=request.GET.get('search')
    data = CustomUser.objects.filter(role='L').order_by('-id')
    landload_request=CustomUser.objects.filter(role='L',status='watting').count()
    if obj in ['watting','approved','rejected']:
        data = CustomUser.objects.filter(role='L',status=obj).order_by('-id')
    landload=CustomUser.objects.filter(role='L').count()
    tenet=CustomUser.objects.filter(role='T').count()
    all_user=CustomUser.objects.all().count()
    return render(request,'landload/app-user-list.html',{
        "data":data,"all_user":all_user,"landload":landload,
        "tenet":tenet,"landload_request":landload_request
    })


@login_required(login_url='/user')
def delete_landload(request,id):
    pass

@login_required(login_url='/user')
def approve_landload(request,pk):
    obj=CustomUser.objects.get(id=pk)
    obj.is_active=True
    obj.status='approved'
    obj.save()
    account_activation_mail(
        obj.first_name+obj.last_name if obj.last_name else "",
        obj.email)
    return JsonResponse(True,safe=False)

@login_required(login_url='/user')
def reject_landload(request,pk):
    obj=CustomUser.objects.get(id=pk)
    obj.is_active=False
    obj.status='rejected'
    obj.save()
    account_rejected_mail(
        obj.first_name+obj.last_name if obj.last_name else "",
        obj.email)
    return JsonResponse(True,safe=False)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView,UpdateView

class EmailTemplateView(SuccessMessageMixin, CreateView):
    form_class = EmailTemplateForm
    model = EmailTemplate
    template_name = "landload/emailtemplate.html"
    success_message = "Added Succesfully"
    def get_success_url(self):
        return reverse('/')
from django.urls import reverse_lazy

class EmailTemplateUpdateView(SuccessMessageMixin, UpdateView):
    model = EmailTemplate
    form_class = EmailTemplateForm
    template_name = "landload/emailtemplate.html"  # Update the template name if needed
    success_message = "Updated Successfully"  # Change success message as needed
    success_url = reverse_lazy('landload:home')  # Update the success URL

    def get_success_url(self):
        # Modify the success URL as needed
        return reverse_lazy('landload:home')
# import json
# def updatetemplate(request,pk):
#     print('uuuuuuuuuuuuuuuuuuuuuuuuuuu')
#     email_template = EmailTemplate.objects.get(id=pk)
    
#     if request.method == 'POST':
#         print(request)
#         json_data = json.loads(request.POST['id_body'])
#         print(json_data)
#         form = EmailTemplateForm(request.POST, instance=email_template)
#         data=request.POST.get('id_body')
#         print("kkkkkkkkkkkkkkkkkkkkkkk",data)
#         if form.is_valid():
#             print('vallllllllllllllllllllllll')
#             form.save()
#             return JsonResponse(True,safe=False)
#         else:
#             print(form.errors)
#         return JsonResponse(False,safe=False)



