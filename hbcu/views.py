from django.shortcuts import render, redirect, get_object_or_404
from .models import College, User
from .forms import UserForm

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

# def add_user(request):
#     if request.method == "POST":
#         uform = UserForm(data = request.POST)
#         # pform = UserProfileForm(data = request.POST)
#         if uform.is_valid():
#         # and pform.is_valid():
#             user = uform.save()
#             # profile = pform.save(commit = False)
#             profile.user = user
#             profile.save()

