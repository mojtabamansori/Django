from django.urls import path
from . import views

urlpatterns = [
    path('saturday', views.saturday),
    path('sunday', views.sunday),

]