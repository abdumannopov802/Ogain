from django.shortcuts import render
from .models import *

def blog_details(request):
    return render(request, 'blog-details.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories})

def main(request):
    return render(request, 'main.html', {})

def shop_details(request):
    return render(request, 'shop-details.html', {})

def shop_grid(request):
    return render(request, 'shop-grid.html', {})

def shopping_cart(request):
    return render(request, 'shoping-cart.html', {})


### Authentication
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm

# # signup page
# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'authentication/sign-up.html', {'form': form})

# # login page
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'authentication/log-in.html', {'form': form})

# # logout page
# def user_logout(request):
#     logout(request)
#     return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        return render(request, 'authentication/log-in.html')
	
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful sign-up
        else:
            for field, errors in signup_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'authentication/sign-up.html', {'signup_form': signup_form})

def user_logout(request):
    logout(request)
    return redirect('home')