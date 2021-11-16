from django.urls import path   
from currences import views

urlpatterns = [
path('', views.index, name="index")
]
