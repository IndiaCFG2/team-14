from django.db import models
from schools import models as school_models

# Create your models here.
class Tech_level(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=20)

    def __str__(self):
        return self.level_name

class Week(models.Model):
    week_id = models.IntegerField(primary_key=True)
    week = models.CharField(max_length=20)

    def __str__(self):
        return self.week

class DName(models.Model):
    d_id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class Grade(models.Model):
    grade_id = models.IntegerField(primary_key=True)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    tech_level = models.ForeignKey('Tech_Level',on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    board = models.ForeignKey('schools.Boards', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    grade = models.ForeignKey('Grade',on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name




