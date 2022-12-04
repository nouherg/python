from django.db import models

# Create your models here.


class OriginalForm(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    date =models.CharField(max_length=200, default='2019-01-01')
    sex = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    maladies = models.CharField(max_length=200)
    wordFile = models.FileField(upload_to='wordFiles/')
    
    def __str__(self):
        return self.firstName

class FakeForm(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default='2019')
    sex = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    maladies = models.CharField(max_length=200)
    wordFile = models.FileField(upload_to='wordFiles/')

    def __str__(self):
        return self.firstName
