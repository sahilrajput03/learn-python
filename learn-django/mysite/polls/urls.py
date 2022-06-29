from django.urls import path

from . import views

urlpatterns = [
	# This matches /polls and /polls/
    path('', views.index, name='index'),

	# This matches /polls/page1 and not /polls/page1/
    path('page1', views.page1, name='index'),
]

# This file is created by my own ~ Sahil

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.

