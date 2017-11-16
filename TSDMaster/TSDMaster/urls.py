"""TSysDocker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from datetime import datetime
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views
from TSDMaster import views
from TSDMaster import forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^admin/', admin.site.urls),
]
