from django.shortcuts import render
from django.conf import settings

# TestSys views here.


def home(request):
    return render(request, 'home.html',
                  {
                      'title': 'Home',
                      'company_name': settings.COMPANY_NAME,
                  })
