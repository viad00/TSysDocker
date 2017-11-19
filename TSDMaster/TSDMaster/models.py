from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contest(models.Model):
    name = models.CharField(max_length=50)
    date_start = models.DateTimeField()
    date_stop = models.DateTimeField()
    problems_file = models.URLField(null=True)
    opened = models.BooleanField(default=True)


class Problem(models.Model):
    problem_id = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    tests = models.TextField()
    contest = models.ForeignKey(Contest)


class Try(models.Model):
    problem = models.ForeignKey(Problem)
    status = models.CharField(max_length=2)
    text = models.TextField(null=True)
    reason = models.CharField(max_length=255, null=True)
    current_test = models.IntegerField(null=True)
    owner = models.ForeignKey(User)
    contest = models.ForeignKey(Contest)


class UserContest(models.Model):
    user = models.OneToOneField(User)
    contest = models.ForeignKey(Contest)
