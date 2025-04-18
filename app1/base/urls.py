"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from home.views import *
from vega.views import *

urlpatterns = [

    path('', home, name='home'),
    path('receipe', receipe, name='receipe'),
    path('delete-receipe/<id>/', delete_receipe, name='delete_receipe'),
    path('update-receipe/<id>/', update_receipe, name='update_receipe'),
    
    path('home', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
