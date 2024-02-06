from testapp import views
from django.urls import path

urlpatterns = [
    path('', views.homeView),
    path('langauge/', views.languageView),
    path('project/', views.projectView),
    path('contact/', views.contactView),

]
