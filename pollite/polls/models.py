from django.db import models

# Create your models herei.

class Question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=50)
    votes= models.IntegerField(default=0)
