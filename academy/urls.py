from django.urls import path
from . import views

# Creating the model
# Decided which url pattern to create
# created url pattern in the main url.py, and forwarded it to student url.py
# created the view
# created the template

urlpatterns = [
    path('course/', views.course, name="courses"),
    path('student/', views.student, name="students"),

    path('<int:id>/', views.student_details, name="student_details"),
    path('add/', views.add_student, name="add_student"),
    path('<int:id>/edit/', views.student_edit, name="student_edit"),
    path('<int:id>/delete/', views.delete_student, name="delete_student"),

    path('course_add/', views.add_course, name="add_course"),
    path('trainer_add/', views.add_trainer, name="add_trainer"),

    path('trainer/', views.trainer, name="trainers"),
]
