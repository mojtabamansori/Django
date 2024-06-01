from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_list),
    path('<int:day>', views.dynamic_days_by_number),
    path('<str:day>', views.dynamic_days, name='days-of-week'),
]