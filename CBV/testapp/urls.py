from django.urls import path
from. import views

urlpatterns = [
    path('hello/',views.helloView.as_view(),),
    path('template/', views.templateCBV.as_view(),),
    path('template2/', views.tt.as_view(),),
]
