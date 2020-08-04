from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class PersonalInfo(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=255, )
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    dob = models.DateField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phone = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname


class EducationalInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)
    program = models.CharField(max_length=255)
    institution = models.CharField(max_length=100)
    course = models.BooleanField(default=0)
    edate1 = models.DateField(max_length=255)
    edate2 = models.DateField(max_length=255)

    def __str__(self):
        return self.program

class ExperienceInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    startingDate = models.DateField(max_length=255)
    endingDate = models.DateField(max_length=255)
    experienceInfo = models.TextField(max_length=255)

    def __str__(self):
        return self.company


class Skills(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255, unique=True)

class Certificate(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=255)
    certificateDate = models.DateField(max_length=255)

class Language(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    language = models.CharField(max_length=255)

