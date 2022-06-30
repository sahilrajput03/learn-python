from django.urls import path

from . import views

urlpatterns = [
	# This matches /polls and /polls/
    path('', views.index, name='index'),

	# This matches /polls/page1/ and /polls/page1 is redirected to /polls/page1/
    path('page1/', views.page1, name='index'),

	#? ADDED NEW URLS FROM DOCS
	#?  Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function.
	# ex: /polls/5/
	path('<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/results/
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
]

# This file is created by my own ~ Sahil

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.

