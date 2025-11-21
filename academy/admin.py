from django.contrib import admin
from .models import Course, Trainer, Student

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','description','duration','trainer','photo']
    list_filter = ['course_name']
    search_fields = ['course_name']
    list_display_links = ['course_name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','enrolled_course','trainer','is_active']
    list_filter = ['first_name','email']
    search_fields = ['email']
    list_editable = ['is_active']
    list_display_links = ['first_name','email']
   

class TrainerAmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','expertise','trainer_photo']
    list_filter = ['first_name','email']
    search_fields = ['expertise']
    list_display_links = ['first_name','email']

admin.site.register(Course,CourseAdmin)
admin.site.register(Trainer,TrainerAmin)
admin.site.register(Student,StudentAdmin)