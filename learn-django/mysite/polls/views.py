from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # loader is used to parse an html template imo ~ Sahil
from .models import Question

# Create your views here.

# Index here specifies the index page for 'polls/' app.
def index(request):
    # RESPONSE 1
    # return HttpResponse("Hello, world. You're at the polls index.")
    # RESPONSE 2
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # output = '<br/>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # RESPONSE 3
    #? USING A TEMPLATE HTML NOW
    # template = loader.get_template('polls/index.html')
    # DOCS: context is a dictionary mapping template variable names to Python objects.
    context = { 'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))

    # RESPONSE 4 (short hand way to make `RESPONSE 3` like we did above)
    return render(request, 'polls/index.html', context)
    # learn: Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote). The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

def page1(request):
    # When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.
    return HttpResponse("Hello, world. I am page 1.")

# new views from docs: https://docs.djangoproject.com/en/4.0/intro/tutorial03/
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)