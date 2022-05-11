from django.urls import path     
from . import views
urlpatterns = [
    path('/blogs/', views.root_method),
    path('/new/', views.new_method),
    path('/create/', views.redirected),
    path('/blogs/<number>/',views.number) 
]

