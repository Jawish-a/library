from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Library(models.ModelForm):
    manager = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    # for the admin panel
    def __str__(self):
        return self.name
