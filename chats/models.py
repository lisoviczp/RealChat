from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __str__(self):
		return str(self.username) or '' 

	def __unicode__(self):
		return unicode(self.username) or u''


class Comment(models.Model):
  author = models.CharField(max_length=50)
  sending_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sending_user')    
  receiving_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiving_user')
  text = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return str(self.text) or '' 

  def __unicode__(self):
  	return unicode(self.text) or u''    