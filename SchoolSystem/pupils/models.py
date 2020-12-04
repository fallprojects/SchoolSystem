from django.contrib.auth.models import User
from django.db import models



class Pupils(models.Model):
    Sex = (
        ('Мужской','Мужской'),
        ('Женский','Женский')
    )
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    sex = models.CharField(max_length=50,null=True,choices=Sex)
    date_of_birth = models.DateTimeField(null=True)
    classes = models.ForeignKey('Class',on_delete=models.SET_NULL,null=True,related_name='pupils')
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.first_name

class Class(models.Model):
    pupil_class = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.pupil_class


