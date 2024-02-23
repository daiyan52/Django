from django.urls import path
from . import views
urlpatterns = [
    path('',views.data_view),
    path('insert/',views.insert_view),
    path('delete/<int:id>',views.delete_view),
    path('update/<int:id>',views.update_view)

]