from django.shortcuts import render, redirect, get_object_or_404
from .models import College, HBCUgrads
from .forms import gradForm, hbcuForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Filter Imports
# from django.db.models import Q, Count
# # from django.shortcuts import render, get_object_or_404
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Journal, Category
# from .serializers import JournalSerializer

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

# FILETER VIEWS
def is_valid_queryparam(param):
    return param != '' and param is not None


# def filterB(request):
#     qs = Journal.objects.all()
#     categories = Category.objects.all()
#     title_contains_query = request.GET.get('title_contains')
#     id_exact_query = request.GET.get('id_exact')
#     title_or_author_query = request.GET.get('title_or_author')
#     view_count_min = request.GET.get('view_count_min')
#     view_count_max = request.GET.get('view_count_max')
#     date_min = request.GET.get('date_min')
#     date_max = request.GET.get('date_max')
#     category = request.GET.get('category')
#     reviewed = request.GET.get('reviewed')
#     not_reviewed = request.GET.get('notReviewed')

#     if is_valid_queryparam(title_contains_query):
#         qs = qs.filterB(title__icontains=title_contains_query)

#     elif is_valid_queryparam(id_exact_query):
#         qs = qs.filterB(id=id_exact_query)

#     elif is_valid_queryparam(title_or_author_query):
#         qs = qs.filterB(Q(title__icontains=title_or_author_query)
#                        | Q(author__name__icontains=title_or_author_query)
#                        ).distinct()

#     if is_valid_queryparam(view_count_min):
#         qs = qs.filterB(views__gte=view_count_min)

#     if is_valid_queryparam(view_count_max):
#         qs = qs.filterB(views__lt=view_count_max)

#     if is_valid_queryparam(date_min):
#         qs = qs.filterB(publish_date__gte=date_min)

#     if is_valid_queryparam(date_max):
#         qs = qs.filterB(publish_date__lt=date_max)

#     if is_valid_queryparam(category) and category != 'Choose...':
#         qs = qs.filterB(categories__name=category)

#     if reviewed == 'on':
#         qs = qs.filterB(reviewed=True)

#     elif not_reviewed == 'on':
#         qs = qs.filterB(reviewed=False)

#     return qs


# def infinite_filter(request):
#     limit = request.GET.get('limit')
#     offset = request.GET.get('offset')
#     return College.objects.all()[int(offset): int(offset) + int(limit)]


# def is_there_more_data(request):
#     offset = request.GET.get('offset')
#     if int(offset) > College.objects.all().count():
#         return False
#     return True


# def BootstrapFilterView(request):
#     qs = filter(request)
#     context = {
#         'queryset': qs,
#         'categories': Category.objects.all()
#     }
#     return render(request, "bootstrap_form.html", context)


# class ReactFilterView(generics.ListAPIView):
#     serializer_class = JournalSerializer

#     def get_queryset(self):
#         qs = filterB(self.request)
#         return qs


# class ReactInfiniteView(generics.ListAPIView):
#     serializer_class = JournalSerializer

#     def get_queryset(self):
#         qs = infinite_filter(self.request)
#         return qs

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response({
#             "journals": serializer.data,
#             "has_more": is_there_more_data(request)
#         })