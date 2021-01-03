from django.db import models


# Create your models here.
class OnlineTrainingCategory(models.Model):
	Name = models.CharField(max_length = 100)
	About = models.TextField(default = 'null')

	def __str__(self):
		return self.Name 

class OnlineTrainingApplicantType(models.Model):
	Name = models.CharField(max_length = 100)
	About = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class OnlineTrainingProgram(models.Model):
	Name = models.CharField(max_length = 50)
	About = models.TextField(default = 'null')
	Price = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'OnlineTrainingPrograms/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')
	Display = models.BooleanField(default = False)
	Position = models.IntegerField(default=1)
	Address = models.TextField(default = 'Leader Factory, Mumbai')
	Dates = models.TextField(default = 'null')
	Category = models.ManyToManyField(OnlineTrainingCategory)
	ApplicantType = models.ManyToManyField(OnlineTrainingApplicantType)
	Language = models.CharField(default = 'Hindi', max_length=50)
	WhatYouWillLearn = models.TextField(default='null')
	FreeMaterials = models.TextField(default = 'null')
	DaywiseSchedule = models.TextField(default = 'null')
	SpecialAttractions = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class OnlineTrainingApplicant(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CourseId = models.IntegerField(default=0)
	Confirmed = models.BooleanField(default = False)
	Address = models.TextField(default='null')

	def __str__(self):
		return self.Name

class OnlineClient(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CorpName = models.CharField(max_length = 100, default='null')
	Position = models.CharField(max_length = 100, default='null')
	Subject = models.TextField(default='null')

	def __str__(self):
		return self.Name
