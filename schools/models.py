from django.db import models

# Create your models here.
#Represent Boards
class Boards(models.Model):
    board_id=models.IntegerField()
    board_name=models.CharField(max_length=100)

    def __str__(self):
        return self.board_name


#Represents School 
class Schools(models.Model):
    school_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=200)
    school_city = models.CharField(max_length=100)
    school_state = models.CharField(max_length=200)
    board = models.ForeignKey('Boards', default=1,on_delete=models.CASCADE)
    registration_date = models.DateField()
    total_teachers = models.IntegerField()
    total_students = models.IntegerField()

    def __str__(self):
        return self.school_name




