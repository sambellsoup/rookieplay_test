from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import os
import requests

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    print("Testing DB")
    print("Testing Virtual Environment")
    print("Testing Pickle Folder")
    print("Testing Views")
    print("Testing Document Upload Model")
    return HttpResponse('Hello! ' * times)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
