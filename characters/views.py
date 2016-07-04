from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from pprint import pformat

@login_required
def index(request):
    return HttpResponse('Logged in as ' + request.user.username)
