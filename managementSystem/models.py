from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pin_code = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
