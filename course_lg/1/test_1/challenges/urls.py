from django.urls import path
from . import views

urlpatterns = [
    path('edit-profile',  views.edit_profile),
    path('user-setting',  views.index),
    
]