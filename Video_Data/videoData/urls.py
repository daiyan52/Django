from django.urls import path
from .views import videoView

app_name = 'videoData'
urlpatterns = [
    path('uploadVideo/', videoView, name='uploadVideo'),
]
