from django.contrib import admin
from .models import Library, Book, Auther, Genre, Membership, Member, LibraryLog
# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Auther)
admin.site.register(Genre)
admin.site.register(Membership)
admin.site.register(Member)
admin.site.register(LibraryLog)