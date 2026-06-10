from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Analytics', 'Analytics'),
        ('FinTech', 'FinTech'),
        ('Tools', 'Tools'),]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    level = models.IntegerField(default=80)
    
    def __str__(self):
        return self.name