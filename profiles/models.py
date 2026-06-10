from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    certificate = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    career_goal = models.TextField()
    image = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return self.full_name