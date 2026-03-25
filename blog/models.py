from django.db import models
from django.contrib.auth.models import User
class Blog(models.Model):
    title=models.CharField( max_length=50)
    slug=models.SlugField(unique=True)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,choices=[('draft','Draft'),('Published','published')])
    def __str__(self):
        return self.title
    
    
