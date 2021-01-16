from django.db import models
from django.contrib.postgres.fields import ArrayField
import os


# Create your models here.
class Course(models.Model):

	Name = models.CharField(max_length = 50)
	About = models.TextField(default = 'null')
	Price = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'courses/frontpics/', default = 'null')
	Tags = models.TextField(default = 'null')
	videofile1 = models.TextField(default = 'null')
	videofile2 = models.TextField(default = 'null')
	videofile3 = models.TextField(default = 'null')
	videofile4 = models.TextField(default = 'null')
	videofile5 = models.TextField(default = 'null')
	videofile6 = models.TextField(default = 'null')
	videofile7 = models.TextField(default = 'null')
	videofile8 = models.TextField(default = 'null')
	videofile9 = models.TextField(default = 'null')
	videofile10 = models.TextField(default = 'null')
	videofile11 = models.TextField(default = 'null')
	videofile12 = models.TextField(default = 'null')
	videofile13 = models.TextField(default = 'null')
	videofile14 = models.TextField(default = 'null')
	videofile15 = models.TextField(default = 'null')
	videofile16 = models.TextField(default = 'null') 
	videofile17 = models.TextField(default = 'null')
	videofile18 = models.TextField(default = 'null')
	videofile19 = models.TextField(default = 'null')
	videofile20 = models.TextField(default = 'null')
	videofile21 = models.TextField(default = 'null')
	videofile22 = models.TextField(default = 'null')
	videofile23 = models.TextField(default = 'null')
	videofile24 = models.TextField(default = 'null')
	videofile25 = models.TextField(default = 'null')
	videofile26 = models.TextField(default = 'null')
	videofile27 = models.TextField(default = 'null')
	videofile28 = models.TextField(default = 'null')
	videofile29 = models.TextField(default = 'null')
	videofile30 = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class CourseApplicant(models.Model):
	Name = models.CharField(max_length = 40)
	Address = models.TextField(default='null')
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CourseId = models.IntegerField(default=0)
	CourseName = models.CharField(default='null', max_length=50)
	Confirmed = models.BooleanField(default = False)


	
