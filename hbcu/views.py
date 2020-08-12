from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import College, HBCUgrads
from .forms import gradForm, hbcuForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
  all_colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/index.html', context={'colleges':all_colleges})

def listColleges(request):
  colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/list_hbcus.html', context={'colleges':colleges})

def filter(request):
  colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/filter.html', context={'colleges':colleges})

def hbcu_detail(request, pk):
  school = get_object_or_404(College, pk=pk)
  return render(request, "hbcu/hbcu_detail.html", {'colleges':school})

def hbcuGrad(request):
  graduate = HBCUgrads.objects.all().order_by('name')
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

def add_hbcu(request):
    if request.method == 'GET':
        form = hbcuForm()
    else:
        form = hbcuForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='filter')

    return render(request, "hbcu/add_hbcu.html", {"form": form})

# Adding hbcumap.html
def map(request):
    return render(request, 'hbcu/hbcumap.html', {})


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


# FILTER PAGE

def BootstrapFilterView(request):
  qs = College.objects.all()
  college_contains_query = request.GET.get('college_contains')
  id_exact_query = request.GET.get('college_exact')
  # college_or_major_query = request.GET.get('college_or_major')
  
  if college_contains_query != '' and college_contains_query is not None:
      qs = qs.filter(name__icontains=college_contains_query)
    #  icontain is NOT case sensitive but contains IS; i stands for insensitive 
  elif id_exact_query != '' and id_exact_query is not None:
      qs = qs.filter(id=id_exact_query)
    # could have also used: name__iexact

  # elif college_or_major_query != '' and college_or_major_query  is not None:
  #     qs = qs.filter(Q(college__icontains=college_or_major_query) | Q(major__icontains=college_or_major_query)).distinct()
  
  context = {
    'queryset' : qs
  }
  return render(request, "hbcu/filterB.html", context)