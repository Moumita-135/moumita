from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

DeptChoice = [
    ('', 'Depertment'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstYear', 'First Year'),
    ('SecondYear', 'Second Year '),
    ('ThirdYear', 'Third Year'),
    ('FourthYear', 'Fourth Year'),
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstSemester', 'First Semester'),
    ('SecondSemester', 'Second Semester '),
    ('ThirdSemester', 'Third Semester'),
    ('FourthSemester', 'Fourth Semester'),
    ('FifthSemester', 'Fifth Semester'),
    ('SixthSemester', 'Sixth Semester'),
    ('SeventhSemester', 'Seventh Semester'),
    ('EightthSemester', 'Eightth Semester'),
]



class User(AbstractUser):
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    enrollment = models.CharField(max_length=70, null=True, blank=True)
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_cdc = models.BooleanField('Is cdc', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status = models.BooleanField(default=True)



class QuestionCategory(models.Model):
    name = models.TextField(max_length=100, null=True, blank=True)
    owner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)


class Question(models.Model):
    question = RichTextField(null=True, blank=True)
    questioncategory = models.PositiveIntegerField(null=True, blank=True)
    owner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    postedtime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)


class Answer(models.Model):
    answer = models.TextField(max_length=1000)
    questionid = models.PositiveIntegerField(null=True, blank=True)
    solver = models.PositiveIntegerField(null=True, blank=True)
    answertime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    status = models.BooleanField(default=True)


''' class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    exampleFormControlTextarea1 = models.TextField()
    exampleFormControlTextarea2 = models.TextField()
    questioncategory = models.PositiveIntegerField(null=True, blank=True)
    postedtime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.TextField(max_length=100, null=True, blank=True)
    owner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
 '''
 
class Contact(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        exampleFormControlTextarea1 = models.TextField()
        exampleFormControlTextarea2 = models.TextField()
        def __str__(self):
            return self.name



