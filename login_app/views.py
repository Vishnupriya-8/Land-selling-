from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from landapp.models import land
from django.contrib.auth import authenticate,login,logout# Create your views here.
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:

        form = SignUpForm()  # Only create a new form instance for GET requests

    return render(request, 'sign_up.html', {'form': form})



def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('view')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form': form})




def log_out(request):
    logout(request)
    return render(request,'index.html')


def my_plots(request):
    lands = land.objects.filter(owner=request.user) # Fetch lands added by the logged-in user
    return render(request, 'my_plots.html', {'lands': lands})



def view(request):
    return render(request,'view.html')

@login_required
def add_plot(request):
    if request.method == 'POST':
        form = landForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            land = form.save(commit=False)
            land.owner.id = request.user.id  # Set the owner to the logged-in user
            land.save()  # Now save it to the database
            return redirect('my_plots') # Redirect to land list after saving
    else:
        form = landForm()
    return render(request, 'add_plot.html', {'form': form})

# @login_required
def delete_land(request, land_id):
    land1 = get_object_or_404(land, id=land_id, owner=request.user)  # Ensure the user is the owner
    if request.method == "POST":
        land1.delete()  # Delete the land
        return redirect('my_plots')

# @login_required
def edit_land(request, land_id):
    land1 = get_object_or_404(land, id=land_id, owner=request.user)  # Ensure the user is the owner

    if request.method == 'POST':
        form = landForm(request.POST, request.FILES, instance=land1)  # Include request.FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('my_plots')  # Adjust redirect as necessary
    else:
        form = landForm(instance=land1)

    return render(request, 'edit_plot.html', {'form': form, 'land': land})