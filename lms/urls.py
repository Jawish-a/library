"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #  auth links
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    # basic links
    path('', views.homepage, name='homepage'),
    path('404/', views.not_found, name='404'),
    # library links

    # membership links
    path('memberships/', views.membership_list, name='membership_list'),
    path('membership/create/', views.membership_create, name='membership_create'),
    path('membership/<int:membership_id>/update', views.membership_update, name='membership_update'),
    path('membership/<int:membership_id>/delete', views.membership_delete, name='membership_delete'),
    
    # members
    path('membership/<int:membership_id>/members', views.member_list, name='member_list'),
    path('member/create', views.member_create, name='member_create'),
    

    # book links
    path('books/', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/update', views.book_update, name='book_update'),
    path('book/<int:book_id>/delete', views.book_delete, name='book_delete'),
    
    # auther links
    path('authers/', views.auther_list, name='auther_list'),
    path('auther/create/', views.auther_create, name='auther_create'),
    path('auther/<int:auther_id>/update', views.auther_update, name='auther_update'),
    path('auther/<int:auther_id>/delete', views.auther_delete, name='auther_delete'),

    # genre links
    path('genres/', views.genre_list, name='genre_list'),
    path('genre/create/', views.genre_create, name='genre_create'),
    path('genre/<int:genre_id>/update', views.genre_update, name='genre_update'),
    path('genre/<int:genre_id>/delete', views.genre_delete, name='genre_delete'),

    # log links
    path('log/', views.log_list, name='log_list'),
    path('borrow/', views.log_create, name='log_create'),
    # path('return/<int:log_id>/', views.log_update, name='log_return'),
    path('return/<int:log_id>/', views.log_return, name='log_return'),


]
# media and static links
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
