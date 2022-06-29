from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Index here specifies the index page for 'polls/' app.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def page1(request):
    return HttpResponse("Hello, world. I am page1.")