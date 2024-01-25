from django.urls import path
from . import views
urlpatterns = [
    path('', views.Header_view),
    path('Admission/', views.Admission_view),
    path('Sports/', views.Sports_view),
    path('Placement/', views.Placement_view)
]
