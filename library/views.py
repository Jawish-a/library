from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm, LibraryForm, MembershipForm, BookForm, AutherForm, GenreForm
from .models import Library, Membership, Member, Book, Auther, Genre

#####################################################################
#       basic views                                                  #
#####################################################################
def homepage(request):
    return render(request, 'homepage.html')

def not_found(request):
    return render(request, '404.html')

#####################################################################
#       auth views                                                  #
#####################################################################

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("homepage")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('homepage')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

#####################################################################
#       library views for admin and staff only                      #
#####################################################################

def library_details(request, library_id=1):
    library_obj = Library.objects.get(id=library_id)
    context = {

    }
    return render(request, 'library_details.html', context)

def library_create(request):
    # only staff can create a library
    if not request.user.is_staff:
        return redirect('404')
    
    form = LibraryForm()
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid:
            library_obj = form.save(commit=False)
            library_obj.manager = request.user
            library_obj.save()
            return redirect('library_details', library_obj.id)
    context = {
        "form": form,
    }
    return render(request, 'library_create.html', context)

def library_update(request, library_id):
    # validate if the user is staff or if its a manager of the library
    library_obj = Library.objects.get(id=library_id)
    if not (request.user.is_staff or request.user == library_obj.owner):
        return redirect('404')

    form = LibraryForm(instance=library_obj)
    if request.method == "POST":
        form = LibraryForm(request.POST, request.FILES, instance=library_obj)
        if form.is_valid():
            form.save()
            return redirect('library_details.html')
    context = {
        "library": library_obj,
        "form":form,
    }
    return render(request, 'library_update.html', context)

def library_delete(request, library_id):
    # only staff can delete library
    if not request.user.is_staff:
        return redirect('404')
    
    library_obj = Library.objects.get(id=library_id)
    library_obj.delete()
    return redirect('')

#####################################################################
#       mempership views                                            #
#####################################################################

def membership_list(request, library_id=1):
    library = Library.objects.get(id=library_id)
    if request.user.is_staff or request.user != library.manager:
        return redirect('404')
    memberships = library.memberships.all()
    context = {
        'memberships': memberships
    }
    return render(request, 'manager/membership_list.html', context)

def membership_create(request, library_id=1):
    library = Library.objects.get(id=library_id)
    if request.user.is_staff or request.user != library.manager:
        return redirect('404')
    form = MembershipForm()
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid:
            membership = form.save(commit=False)
            membership.library = library
            membership.save()
            return redirect('membership_list')
    context = {
        'form': form
    }
    return render(request, 'manager/membership_create.html', context)

def membership_update(request, membership_id, library_id=1):
    library = Library.objects.get(id=library_id)
    if (not request.user.is_staff) or (request.user != library.manager):
        return redirect('404')

    membership = Membership.objects.get(id=membership_id)
    if request.method == "POST":
        form = MembershipForm(instance=membership)
        if form.is_valid():
            form.save()
            return redirect('membership_list')

    context = {
        'form': form,
        'membership': membership
    }
    return render(request, 'membership_list', context)

def membership_delete(request, membership_id):
	Membership.objects.get(id=membership_id).delete()
	return redirect('membership_list')

#####################################################################
#       book views                                                  #
#####################################################################

def book_list(request, library_id=1):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    context = {
        'books': books
    }
    return render(request, 'book/book_list.html', context)

def book_create(request, library_id=1):
    library = Library.objects.get(id=library_id)
    if request.user.is_staff or request.user != library.manager:
        return redirect('404')
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            book = form.save(commit=False)
            book.library = library
            book.save()
            return redirect('book_list')
    context = {
        'form': form
    }
    return render(request, 'book/book_create.html', context)

def book_update(request, book_id, library_id=1):
    library = Library.objects.get(id=library_id)
    if (not request.user.is_staff) or (request.user != library.manager):
        return redirect('404')

    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(instance=book)
        if form.is_valid():
            book.save()
            return redirect('book_list')
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'book_list', context)

def book_delete(request, book_id):
	Book.objects.get(id=book_id).delete()
	return redirect('book_list')

#####################################################################
#       auther views                                                #
#####################################################################

def auther_list(request):
    authers = Auther.all()
    context = {
        'authers': authers
    }
    return render(request, 'auther/auther_list.html', context)

def auther_create(request, library_id=1):
    library = Library.objects.get(id=library_id)
    if request.user.is_staff or request.user != library.manager:
        return redirect('404')
    form = AutherForm()
    if request.method == "POST":
        form = AutherForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('auther_list')
    context = {
        'form': form
    }
    return render(request, 'auther/auther_create.html', context)

def auther_update(request, auther_id, library_id=1):
    library = Library.objects.get(id=library_id)
    if (not request.user.is_staff) or (request.user != library.manager):
        return redirect('404')

    auther = Auther.objects.get(id=auther_id)
    if request.method == "POST":
        form = AutherForm(instance=auther)
        if form.is_valid():
            form.save()
            return redirect('auther_list')
    context = {
        'form': form,
        'auther': auther
    }
    return render(request, 'auther_list', context)

def auther_delete(request, auther_id):
	Auther.objects.get(id=auther_id).delete()
	return redirect('auther_list')

#####################################################################
#       genre views                                                 #
#####################################################################

def genre_list(request):
    genres = Genre.all()
    context = {
        'genres': genres
    }
    return render(request, 'genre/genre_list.html', context)

def genre_create(request, library_id=1):
    library = Library.objects.get(id=library_id)
    if request.user.is_staff or request.user != library.manager:
        return redirect('404')
    form = GenreForm()
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('genre_list')
    context = {
        'form': form
    }
    return render(request, 'genre/genre_create.html', context)

def genre_update(request, genre_id, library_id=1):
    library = Library.objects.get(id=library_id)
    if (not request.user.is_staff) or (request.user != library.manager):
        return redirect('404')

    genre = Genre.objects.get(id=genre_id)
    if request.method == "POST":
        form = GenreForm(instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    context = {
        'form': form,
        'genre': genre
    }
    return render(request, 'genre_list', context)

def genre_delete(request, genre_id):
	Genre.objects.get(id=genre_id).delete()
	return redirect('genre_list')
