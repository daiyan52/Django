"""
URL configuration for CBV_CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from testapp.views import StudentList,StudentDetail,StudentCreate,StudentUpdate,StudentDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StudentList.as_view(), name='StudentList'),
    path('<int:pk>/',StudentDetail.as_view(), name='StudentDetail'),
    path('create/',StudentCreate.as_view()),
    path('update/<int:pk>/',StudentUpdate.as_view()),
    path('delete/<int:pk>/',StudentDelete.as_view())
]
