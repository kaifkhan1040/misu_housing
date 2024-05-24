from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.landload_list, name='landload_list'),
    path('approve_landload/<int:pk>', views.approve_landload, name='approve_landload'),
    path('reject_landload/<int:pk>', views.reject_landload, name='reject_landload'),

]