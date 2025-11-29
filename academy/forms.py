from django import forms
from .models import Student,Course,Trainer

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model= Trainer
        fields= '__all__'