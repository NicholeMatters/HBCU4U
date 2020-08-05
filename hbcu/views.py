from django.shortcuts import render, redirect
from .models import College

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
  all_colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/index.html', context={'hbcu':all_colleges})

def filter(request):
  colleges = College.objects.all()
  return render(request, 'hbcu/filter.html', context={'hbcu':colleges})

# def hbcu_detail(request, pk):
#   school = get_object_or_404(College, pk=pk)
#   return render(request, "hbcu/hbcu_detail.html", {'hbcu':school})


@login_required
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
         
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'hbcu/signup.html', {'form': form})