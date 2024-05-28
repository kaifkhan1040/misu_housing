from django.urls import path
from . import views
from .views import EmailTemplateView,EmailTemplateUpdateView


urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.landload_list, name='landload_list'),
    path('approve_landload/<int:pk>', views.approve_landload, name='approve_landload'),
    path('reject_landload/<int:pk>', views.reject_landload, name='reject_landload'),
    path('emailtemp/', EmailTemplateView.as_view(), name='EmailTemplate'),
    path('emailtemplate/update/<int:pk>/', EmailTemplateUpdateView.as_view(), name='EmailTemplateUpdate'),
    # path('emailtemplate/update/save/<int:pk>/', views.updatetemplate, name='EmailUpdateTemplate'),


]