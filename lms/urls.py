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
    path('memberships/', views.membership_list, name='memberships_list'),
    path('memberships/create/', views.membership_create, name='memberships_create'),
    path('memberships/<int:membership_id>/update', views.membership_update, name='memberships_update'),
    path('memberships/<int:membership_id>/delete', views.membership_delete, name='memberships_delete'),
    
    # book links
    # path('books/', views.book_list, name='books_list'),
    # path('books/create/', views.book_create, name='books_create'),
    # path('books/<int:book_id>/update', views.book_update, name='books_update'),
    # path('books/<int:book_id>/delete', views.book_delete, name='books_delete'),
    
]
# media and static links
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
