from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def movie(request):
  return render(request, 'movies.html')

def login_view(request):
  return render(request,'login.html')

def auth_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})