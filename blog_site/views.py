from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    ###render HttpResponse
    # return HttpResponse('Hello world')

    return render(request, 'welcome.html')
