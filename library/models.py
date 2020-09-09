from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Library(models.Model):
    manager = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="managers")
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    # for the admin panel
    def __str__(self):
        return self.name
class Membership(models.Model):
    periods = (
		("M", "Monthly"),
		("Y", "Yearly"),
	)
    name = models.CharField(max_length=120)
    period = models.CharField(max_length=1, choices=periods)
    is_active = models.BooleanField(default=False)

class Member(models.Model):
    genders = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=1, choices=genders)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    membership = models.OneToOneField(Membership, default=1 ,on_delete=models.CASCADE, related_name="mempership")
