from django.shortcuts import render
from academy.models import Course, Student, Trainer

def home(request):   
    active_students = Student.objects.filter(is_active=True).count()
    running_courses = Course.objects.filter(is_running=True).count()
    total_trainers = Trainer.objects.count()

    context = {
        "active_students": active_students,
        "running_courses": running_courses,
        "total_trainers": total_trainers,
    }
    return render(request, "home.html", context)
