from django.db import models
from django.utils import timezone

# Create your models here.
# the parameters models.Model means that Post is a Django Model, so Django knows 
# that is should be saved in the database.
class Post(models.Model):
	# models.foreignkey is a link to another model
	author = models.ForeignKey('auth.User')
	# models.charField is how you define text with a limited number of characters
	title = models.CharField(max_length = 200)
	# models.TextField is for long text without a limit.  
	text = models.TextField()
	# models.dateandtimefield is for date and time
	created_date = models.DateTimeField(
			default = timezone.now)
	published_date = models.DateTimeField(
			blank = True, null = True)
	
	# function publish is for class Post.  It assigns the publish_date attribute
	# of an instance of the post class to value from timezone.now()
	# Saves the changes to the publish date.
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	# the function __str__ is for the class Post.  It returns the attribute title
	# from an instance of the class Post.
	def __str__(self):
		return self.title