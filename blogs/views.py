from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Blog

def index(request):
    # return HttpResponse('Hello, you are in blogs app')
    blogs = Blog.objects.all()
    output = ', '.join([str(blog) for blog in blogs])
    return HttpResponse(output)
