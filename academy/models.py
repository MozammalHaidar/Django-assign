from django.db import models

# Create your models here.

class Course(models.Model):
    Week_choices = [
        (6, "6 Weeks"),
        (8, "8 Weeks"),
        (12, "12 Weeks"),
    ]
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(choices=Week_choices)
    photo = models.ImageField(upload_to='courses')
    trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True, blank=True)
    is_running = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=50)
    trainer_photo = models.ImageField(upload_to='trainer')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images', default = 'default.jpg', blank=True, null=True)
    enrolled_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='students'
    )
    trainer = models.ForeignKey(
        Trainer, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"
   
