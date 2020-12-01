from django.db import models

class Pupils(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    sex = models.CharField(max_length=50,null=True)
    date_of_birth = models.CharField(max_length=50,null=True)
    classes = models.ForeignKey('Class',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.first_name

class Class(models.Model):
    pupil_class = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.pupil_class

