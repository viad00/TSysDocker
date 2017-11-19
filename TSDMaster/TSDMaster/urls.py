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
from django.conf import settings
from TSDMaster import views
from TSDMaster import forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all_contests$', views.all_contests, name='all_contests'),
    url(r'^enter_contest$', views.enter_contest, name='enter_contest'),
    url(r'^contest$', views.contest, name='contest'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'company_name': settings.COMPANY_NAME,
                }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^admin/', admin.site.urls),
]
