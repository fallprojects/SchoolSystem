from django.db import models


class Pupils(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    sex = models.CharField(max_length=50,null=True)
    date_of_birth = models.CharField(max_length=50,null=True)
    classes = models.ForeignKey('Class',on_delete=models.SET_NULL,null=True)

class Class(models.Model):
    pupile_class = models.CharField(max_length=50, null=True)

