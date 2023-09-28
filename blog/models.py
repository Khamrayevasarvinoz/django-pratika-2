
from django.db import  models
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False
    
class Vidoheader(models.Model):
    vidio = models.FileField()

    
    


class Course(models.Model):
    title = models.CharField(max_length=200)
    about = RichTextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to='courses')
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teacher')
    level = models.IntegerField()
    about = RichTextField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    picture = models.ImageField(upload_to='project')
    title = models.CharField(max_length=100)
    about = RichTextField()
    vidio = models.FileField()

    def __str__(self):
        return self.title
    
class Level(models.Model):
    image = models.ImageField(upload_to='level')
    title = models.CharField(max_length=100)
    reading = models.IntegerField()
    listening = models.IntegerField()
    writing = models.IntegerField()
    speaking = models.IntegerField()

    def str(self):
        return self.title
    
class Students(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=200)
    extnumber = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    stu_day = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname
    
class Contact(models.Model):
    tel_nomer = models.CharField(max_length=200)
    email = models.EmailField()
    level = models.CharField(max_length=100)
    message = RichTextField()

    def __str__(self):
        return self.level
    


    


