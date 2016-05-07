from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import ListField

class Question(models.Model):
	text = models.TextField()
	tags = ListField()

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField()
	votes = models.IntegerField(default=0)
