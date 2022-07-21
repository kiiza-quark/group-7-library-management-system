import datetime
from urllib.request import AbstractBasicAuthHandler 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class Book(models.Model):
    title = models.CharField(max_length=200)
    edition = models.PositiveIntegerField(null=True, blank=True)
    author = models.CharField(max_length=200)
    ISBN= models.PositiveIntegerField(null=False,blank=False)
    subject_area = models.CharField(max_length=50)
    book_cover = models.ImageField(upload_to='bookcovers', blank=False, default='Book cover')

    def __str__(self):
        return str(self.title) + "" +str(self.ISBN) 


class Student(models.Model):
    first_name = models.CharField(max_length= 120)
    last_name = models.CharField(max_length=120)
    password = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    gender_choices = [
        ('M','Male'),
          ('F','Female'),  
    ]
    gender = models.CharField(max_length=10, choices=gender_choices, default='Your sex')  
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name} {self.reg_no} {self.course}'
        
def expiry():   
    return datetime.today() + timedelta(days=10)

def fine():
    now = datetime.now()
    diff = now 
    if diff.days <= 0:
        return 'None'
    elif diff.days >= 3:
        return 5000
    elif diff.days >= 10:
        return 15000
    
class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    ISBN = models.ForeignKey(Book, on_delete=models.PROTECT)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=None)
    fine = models.PositiveIntegerField(default=None)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.student, self.issued_date, self.expiry_date, self.fine)

