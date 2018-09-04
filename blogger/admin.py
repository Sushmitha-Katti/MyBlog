from django.contrib import admin
from blogger.models import BlogPost, Comment


admin.site.register(BlogPost)
admin.site.register(Comment)