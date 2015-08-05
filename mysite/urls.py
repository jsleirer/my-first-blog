from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	# for every URL that starts with admin/ Django will find
	# a corresponding view.  
    url(r'^admin/', include(admin.site.urls)),
	# Django will now redirect everything that comes to
	# http://127.0.0.01:8000/ to blog.urls, what part of the 
	# code directs it to http://127.0.0.01:8000/  ? 
	url(r'', include('blog.urls')),
]
