from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
    path('third/', views.third),
    path('forth/', views.forth),
    path('fifth/', views.fifth),
]
