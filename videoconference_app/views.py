from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
import random

active_rooms = {}  # Global dictionary to keep track of active rooms and their participant counts

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'login.html', {'success': "Registration successful. Please login."})
            except IntegrityError:
                error_message = "A user with that username already exists."
                return render(request, 'register.html', {'error': error_message, 'form': form})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message, 'form': form})

    return render(request, 'register.html', {'form': RegisterForm()})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')

@login_required
def random_call(request):
    global active_rooms

    # Find a room with less than 2 participants
    roomID = None
    for room, count in active_rooms.items():
        if count < 2:
            roomID = room
            active_rooms[room] += 1
            break

    if roomID is None:
        # Create a new room if no room with less than 2 participants is found
        roomID = str(random.randint(1000, 9999))
        active_rooms[roomID] = 1
    else:
        # Remove the room from active_rooms if it reaches 2 participants
        if active_rooms[roomID] >= 2:
            del active_rooms[roomID]
    
    return redirect("/meeting?roomID=" + roomID)
