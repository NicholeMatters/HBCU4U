from django.shortcuts import render, redirect, get_object_or_404
from .models import College

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


