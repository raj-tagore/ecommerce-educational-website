from django.db import models

# Create your models here.
class TrainingProgram(models.Model):
	Name = models.CharField(max_length = 50)
	About = models.TextField(default = 'null')
	Price = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'TrainingPrograms/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')
	Display = models.BooleanField(default = False)
	Address = models.TextField(default = 'Leader Factory, Mumbai')
	Dates = models.TextField(default = 'null')

class TrainingApplicant(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CourseId = models.IntegerField(default=0)
	Confirmed = models.BooleanField(default = False)

class Client(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CorpName = models.CharField(max_length = 100, default='null')
	Position = models.CharField(max_length = 100, default='null')
	Subject = models.TextField(default='null')
