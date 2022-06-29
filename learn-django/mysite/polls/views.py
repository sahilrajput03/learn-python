from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Index here specifies the index page for 'polls/' app.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def page1(request):
    # When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.
    return HttpResponse("Hello, world. I am page 1.")