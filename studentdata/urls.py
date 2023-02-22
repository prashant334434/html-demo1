"""studentdata URL Configuration

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
from studentdata import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('reg/',view.reg),
    path('viewdata/',view.viewdata),
    path('viewall/',view.viewall),
    path('viewbybtime/',view.viewbybtime),
    path('fviewbybtime/<str:btime>',view.fviewbybtime),
    path('viewbyregno/',view.viewbyregno),
    path('fviewbyregno/<str:regno>',view.fviewbyregno),
    path('viewbyname/',view.viewbyname),
    path('fviewbyname/<str:uname>',view.fviewbyname),
    path('delete/',view.delete),
    path('update/',view.update),
    path('fupdate/<str:update>',view.fupdate),
    path('fee/',view.fee),
    path('subfee/',view.subfee),
    path('subfee1/<str:fregno>',view.subfee1),
    path('viewfee/',view.viewfee),
    path('fviewfee/<str:fregno>',view.fviewfee),
    path('passout/',view.passout),
]
