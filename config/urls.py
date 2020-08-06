"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from hbcu import views as hbcu_views

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hbcu_views.index, name='index'),
    path('hbcu/filter', hbcu_views.listColleges, name='filter'),
    path('hbcu/<int:pk>/hbcu_detail', hbcu_views.hbcu_detail, name='hbcu_detail'),
    path('hbcu/map', hbcu_views.map, name='map'),
    path('hbcu/graduates', hbcu_views.hbcuGrad, name='hbcugrads'),
    path('hbcu/addGraduate/', hbcu_views.add_grad, name='add_grad'),

    # user urls
    url(r'^$', hbcu_views.home, name='home'),
    url(r'^signup/$', hbcu_views.signup, name='signup'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

