from django.db import models

#? Create your models here.

# In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

# Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
	#  models.CharField, for example, requires that you give it a max_length. That’s used not only in the database schema, but in validation, as we’ll soon see.
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	# A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

# Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.