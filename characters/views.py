from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Character

@login_required
def index(request):
    return HttpResponse('Logged in as ' + request.user.username)

@login_required
def update_character(request):
    context = {}
    return render(request, 'characters/update_character.html', context)
