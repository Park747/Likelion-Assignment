"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('visitorlog_create', views.visitorlog_create, name="visitorlog_create"),
    path('visitorlog_detail/<int:log_pk>', views.visitorlog_detail, name="visitorlog_detail"),
    path('showroom', views.showroom, name="showroom"),
    path('songrequest', views.songrequest, name="songrequest"),
    path('delete//<int:log_pk>', views.delete, name="delete"),
    path('detail/<int:log_pk>/edit', views.edit, name="edit")
]
