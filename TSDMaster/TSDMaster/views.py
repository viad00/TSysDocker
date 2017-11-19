from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.messages import add_message, SUCCESS
from TSDMaster import forms
from TSDMaster.models import Contest, UserContest, Try, Problem

# TestSys views here.


def home(request):
    return render(request, 'home.html',
                  {
                      'title': 'Home',
                      'company_name': settings.COMPANY_NAME,
                  })


def register(request):
    if request.method == 'POST':
        form = forms.BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            add_message(request, SUCCESS, 'You may login now')
            return redirect('login')
        return render(request, 'register.html',
                      {
                          'errors': form.errors,
                          'form': forms.BootstrapUserCreationForm,
                          'title': 'Register',
                          'company_name': settings.COMPANY_NAME,
                      })
    else:
        return render(request, 'register.html',
                      {
                          'form': forms.BootstrapUserCreationForm,
                          'title': 'Register',
                          'company_name': settings.COMPANY_NAME,
                      })


def all_contests(request):
    return render(request, 'all_contests.html', {
        'contests': Contest.objects.filter(opened=True),
        'title': 'All contests',
        'company_name': settings.COMPANY_NAME,
    })


def enter_contest(request):
    # TODO: Check contest available
    try:
        conq = UserContest.objects.get(user=request.user)
        conq.contest_id = int(request.GET['id'])
        conq.save()
    except Exception:
        UserContest(user=request.user, contest_id=int(request.GET['id'])).save()
    return redirect('/contest')


def contest(request):
    cur_contest = UserContest.objects.get(user=request.user).contest
    problems = Problem.objects.filter(contest=cur_contest)
    trys = Try.objects.filter(contest=cur_contest)
    users = set()
    problems_trys = {}
    for tryi in trys:
        if tryi.owner not in users:
            users.add(tryi.owner)
            problems_trys[tryi.owner] = {}
            for problem in problems:
                problems_trys[tryi.owner][problem] = [0, False]
        if not problems_trys[tryi.owner][tryi.problem]:
            if tryi.status == 'PE' or tryi.status == 'WA' or tryi.status == 'TL' or tryi.status == 'ML' or tryi.status == 'AR':
                problems_trys[tryi.owner][tryi.problem][0] += 1
            elif tryi.status == 'OK':
                problems_trys[tryi.owner][tryi.problem][1] = True
    # TODO: Presentation
    return render(request, 'contest.html', {
        'contest': cur_contest,
        'problems': problems,
        'competitors': users,
        'problem_trys': problems_trys,
        'title': 'Contest',
        'company_name': settings.COMPANY_NAME,
    })
