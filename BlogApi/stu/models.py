from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=32, unique=True)
    spwd = models.CharField(max_length=32)

    def __str__(self):
        return u'Student: %s'%self.sname