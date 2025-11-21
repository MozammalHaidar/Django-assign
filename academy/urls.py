from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course, name="courses"),
    path('student/', views.student, name="students"),
    path('trainer/', views.trainer, name="trainers"),
]