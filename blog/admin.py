from django.contrib import admin
from .models import Post

# Register your models here.
# Registering the model makes the model visible on the admin page
admin.site.register(Post)