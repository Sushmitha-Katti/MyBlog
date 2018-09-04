from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE,null = True)

	def __str__(self):
		return f"{self.post.title} | {self.text[:30]}"

	



