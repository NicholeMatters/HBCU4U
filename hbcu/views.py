from django.shortcuts import render
from .models import College

# Create your views here.
def index(request):
  all_colleges = College.objects.all().order_by('name')
  return render(request, 'hbcu/index.html', context={'hbcu':all_colleges})