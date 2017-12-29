from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	ower = models.ForeignKey(User,1)
	def __str__(self):
		return self.text
class Entry(models.Model):
	topic = models.ForeignKey(Topic,1)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'entries'
	def __str__(self):
		return self.text[:50]+'...'