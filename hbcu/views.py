from django.shortcuts import render, redirect, get_object_or_404
from .models import College, HBCUgrads
from .forms import gradForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
  all_colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/index.html', context={'colleges':all_colleges})

def listColleges(request):
  colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/filter.html', context={'colleges':colleges})

def hbcu_detail(request, pk):
  school = get_object_or_404(College, pk=pk)
  return render(request, "hbcu/hbcu_detail.html", {'colleges':school})

def map(request):
  colleges = College.objects.all().order_by('state')
  return render(request, 'hbcu/map.html', context={'colleges':colleges})

def hbcuGrad(request):
  graduate = HBCUgrads.objects.all().order_by('last_name')
  return render(request, 'hbcu/hbcugrads.html', context={'graduates':graduate})

def add_grad(request):
    if request.method == 'GET':
        form = gradForm()
    else:
        form = gradForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='hbcugrads')

    return render(request, "hbcu/add_grad.html", {"form": form})

# User login
@login_required
def home(request):
    return render(request, 'hbcu/index.html')

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