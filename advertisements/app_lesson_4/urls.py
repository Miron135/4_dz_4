from django.urls import path
from .views import index, empty

urlpatterns = [
    path('lesson_4/', index),
    path('', empty),   
]
