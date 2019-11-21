from django.http import HttpResponse
from django.shortcuts import render_to_response


def hello(request):
    return HttpResponse("{“Message”: “Hello World!”}")

def home(request):
    return render_to_response('index.html')
