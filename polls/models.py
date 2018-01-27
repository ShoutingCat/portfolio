from django.db import models


# Create your models here.

class Question(models.Model):
    qeustion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # __str__ on Pyton 3
        return self.qeustion_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # __str__ on Python 3
        return self.choice_text
