from django.db import models

# Create your models here.
class School_Analysis(models.Model):
    date = models.DateField()
    school = models.ForeignKey('schools.Schools', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = ('date', 'school')


class Course_Analysis(models.Model):
    date = models.DateField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    week = models.ForeignKey('courses.Week', on_delete=models.CASCADE)
    Dname = models.ForeignKey('courses.DName', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = ('date', 'course','week','Dname')

