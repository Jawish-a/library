from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

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
    library = models.ForeignKey(Library, default=1, related_name='memberships', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    period = models.CharField(max_length=1, choices=periods)

class Member(models.Model):
    genders = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=1, choices=genders)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="members")
    membership = models.ForeignKey(Membership, default=1 ,on_delete=models.CASCADE, related_name="mempership")
    is_active = models.BooleanField(default=False)


class Book(models.Model):
    name = models.CharField(max_length=191)
    auther = models.ForeignKey("Auther", on_delete=models.CASCADE, related_name="books")
    year = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(10)], unique=True)
    cover = models.ImageField(upload_to='book_covers', null=True, blank=True)
    # if the genre is deleted set the value to null
    # many to many relationship because its gonna be many books can have many genre 
    genre = models.ManyToManyField("Genre", related_name='genres')
    copies = models.IntegerField(default=1)
    library = models.ForeignKey(Library, on_delete=models.PROTECT, related_name="books")
    def __str__(self):
        return self.name
class Auther(models.Model):
    name = models.CharField(max_length=191)
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=191)
    def __str__(self):
        return self.name

class LibraryLog(models.Model):
    library = models.OneToOneField(Library, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrow_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(null=True, blank=True)