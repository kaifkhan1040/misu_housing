"""
URL configuration for housing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('supadmin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user/',include(('users.urls','user'),namespace='user')),
    path('user/', include('django.contrib.auth.urls')),
    path('admin/',include(('customadmin.urls','customadmin'),namespace='customadmin')),
    path('landload/',include(('landload.urls','landload'),namespace='landload')),
    path('tenat/',include(('tenat.urls','tenat'),namespace='tenat')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
