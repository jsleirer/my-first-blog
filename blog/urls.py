from django.conf.urls import url
from . import views

urlpatterns = [
	# Only an empty string will match becase of ^$ regex.  
	# Tells Django that http://127 is the right place to go
	# if someone enters http://127
	url(r'^$', views.post_list, name='post_list'),
]