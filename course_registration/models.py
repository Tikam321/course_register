from django.db import models
from django.contrib.auth.models import User



class Course_Registration(models.Model):
    professor = models.CharField(max_length=22,default=None)
    course_name = models.CharField(max_length=25,default=None)
    course_validity = models.IntegerField(default=None)
    fees = models.IntegerField(default=None)
    timing = models.DateTimeField(default=None)

cd ..

    def __str__(self):
        return self.course_name

class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course_Registration, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
