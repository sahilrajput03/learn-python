from django.db import models

# This is Python’s standard datetime module
import datetime
# This is Django’s time-zone-related utilities in `django.utils.timezone` (Learn timezone handling DOCS in django: https://docs.djangoproject.com/en/4.0/topics/i18n/timezones/).
from django.utils import timezone

#? Create your models here.

# In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

# Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
	#  models.CharField, for example, requires that you give it a max_length. That’s used not only in the database schema, but in validation, as we’ll soon see.
    pub_date = models.DateTimeField('date published')

    # It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
    def __str__(self):
        return self.question_text

    # custom method to this model:
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	# A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

    def __str__(self):
        return self.choice_text

# Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

"""
(Source<below> and LEARN): All about the models api, learn from: https://docs.djangoproject.com/en/4.0/intro/tutorial02/#playing-with-the-api

# Usefull ness of __str__ ?
#* Without __str__ 
# Question.objects.all()
# <QuerySet [<Question: Question object (1)>]>

#* WITH __str__
# Question.objects.all()
# <QuerySet [<Question: What's new?>]>

#*** DJANGO DOCS: Django provides a rich database lookup API that's entirely driven by keyword arguments.
# Question.objects.filter(id=1)
# <QuerySet [<Question: What's new?>]>

#*** DJANGO DOCS: Question.objects.filter(question_text__startswith='What')
# <QuerySet [<Question: What's new?>]>


# Question.objects.get(id=2)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/usr/lib/python3.10/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/usr/lib/python3.10/site-packages/django/db/models/query.py", line 496, in get
    raise self.model.DoesNotExist(
polls.models.Question.DoesNotExist: Question matching query does not exist.

#*** Question.objects.get(pk=1)
# <Question: What's new?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True


# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

"""
