from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateTimeField(auto_now=True)
    age = models.CharField(max_length=250)
    genders = models.CharField(max_length=250)
    pno = models.CharField(max_length=250)
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    cources = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    materials = models.CharField(max_length=250)

    def __str__(self):
        return self.name
