from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('pdf/', views.pdf, name='pdf'),
]