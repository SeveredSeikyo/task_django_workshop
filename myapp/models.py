from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      title=models.CharField(max_length=150)
      subtitle=models.CharField(max_length=250)
      content=models.TextField()
      published_on=models.DateTimeField(auto_now_add=True)