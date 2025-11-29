from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Trainer, Student
from .forms import StudentForm
from .forms import CourseForm
from .forms import TrainerForm
from django.contrib.auth.decorators import login_required, permission_required

def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, "course.html", context)

def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, "trainer.html", context)

def student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "student.html", context)

@login_required
@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST, request.FILES)  

        if form.is_valid():
            form.save()
            return redirect("students")  

        else:
            print(form.errors)

    else:
        form = StudentForm()  

    context = {'form': form}
    return render(request, 'add_student.html', context)

@login_required
@permission_required('academy.student_details', raise_exception=True)
def student_details(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student':student
    }
    return render(request, "student_details.html", context)

@login_required
@permission_required('academy.student_edit', raise_exception=True)

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    trainers = Trainer.objects.all()

    if request.method == "POST":
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')

        course_id = request.POST.get('enrolled_course')
        if course_id and course_id.isdigit():
            student.enrolled_course = Course.objects.get(id=int(course_id))
        else:
            return render(request, "student_edit.html", {
                "student": student,
                "courses": courses,
                "trainers": trainers,
                "error": "Invalid course selected!"
            })

        trainer_id = request.POST.get('trainer')
        if trainer_id and trainer_id.isdigit():
            student.trainer = Trainer.objects.get(id=int(trainer_id))
        else:
            return render(request, "student_edit.html", {
                "student": student,
                "courses": courses,
                "trainers": trainers,
                "error": "Invalid trainer selected!"
            })

        student.is_active = request.POST.get('is_active') == "on"
        student.save()

        return redirect('student_details', id=student.id)  

    return render(request, "student_edit.html", {
        "student": student,
        "courses": courses,
        "trainers": trainers,
    })

@login_required
@permission_required('academy.delete_student', raise_exception=True)
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students')


@login_required
@permission_required('academy.add_course', raise_exception=True)
def add_course(request):
    if request.method == "POST":
        print(request.POST)
        form = CourseForm(request.POST, request.FILES)  

        if form.is_valid():
            form.save()
            return redirect("courses")  

        else:
            print(form.errors)

    else:
        form = CourseForm()  
        
    context = {'form': form}
    return render(request, 'add_course.html', context)

@login_required
@permission_required('academy.add_trainer', raise_exception=True)
def add_trainer(request):
    if request.method == "POST":
        print(request.POST)
        form = TrainerForm(request.POST, request.FILES)  

        if form.is_valid():
            form.save()
            return redirect("Trainers")  

        else:
            print(form.errors)

    else:
        form = TrainerForm()  
        
    context = {'form': form}
    return render(request, 'add_trainer.html', context)

