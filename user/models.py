from django.db import models
from django.contrib.postgres.fields import ArrayField
from courses.models import Course

# Create your models here.
class User(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Password = models.CharField(max_length = 50)
	Phone = models.BigIntegerField(default = 9898989898)
	Premium = models.BooleanField(default = False)
	Courses = models.ManyToManyField(Course) 
	
	def __str__(self):
		return self.Name

class ThreeFeaturedPic(models.Model):
	Picture = models.FileField(upload_to='', default='null')
	URLPointer = models.TextField(default='null')

#class ContactRequest(models.Model):



