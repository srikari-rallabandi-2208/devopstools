"""devopstools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from devopstools.views import save_top_results, top_results, ps_results, save_ps_results

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/save-top-results/', save_top_results, name='save_top_results'),
    path('top-results/', top_results, name='top_results'),
    path('api/save-ps-results/', save_ps_results, name='save_ps_results'),
    path('ps-results/', ps_results, name='ps_results'),
]
