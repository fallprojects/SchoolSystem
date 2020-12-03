from django.db import models

from pupils.models import Class,Pupils


class Teacher(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    otchestvo = models.CharField(max_length=50,null=True)
    subject = models.ForeignKey('Subject',models.SET_NULL,null=True)
    classes = models.ForeignKey(Class, models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

class Subject(models.Model):
    subject = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.subject

class PupilstoObjects(models.Model):
    subjects = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,related_name='to_subjects')
    classes = models.ManyToManyField(Class,null=True)


class Grade(models.Model):
    grade = models.ForeignKey(Pupils, on_delete=models.SET_NULL, null=True,related_name='grades')
