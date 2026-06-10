from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateField(blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField()
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title