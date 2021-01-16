from django.db import models

# Create your models here.
'''TrainingCategories = (	('1', 'No Category'),
						('2', 'Insurance'),
						('3', 'Sales'),
						('4', 'Network Marketing'),
						('5', 'Business'),
						('6', 'Self Development'))'''

class TrainingCategory(models.Model):
	Name = models.CharField(max_length = 100)
	About = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class TrainingApplicantType(models.Model):
	Name = models.CharField(max_length = 100)
	About = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class TrainingProgram(models.Model):
	Name = models.CharField(max_length = 100)
	About = models.TextField(default = 'null')
	Price = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'TrainingPrograms/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')
	Display = models.BooleanField(default = False)
	Position = models.IntegerField(default=1)
	Address = models.TextField(default = 'Leader Factory, Mumbai')
	Dates = models.CharField(default = 'null', max_length=100)
	Category = models.ManyToManyField(TrainingCategory)
	ApplicantType = models.ManyToManyField(TrainingApplicantType)
	Language = models.CharField(default = 'Hindi', max_length=50)
	WhatYouWillLearn = models.TextField(default='null')
	FreeMaterials = models.TextField(default = 'null')
	DaywiseSchedule = models.TextField(default = 'null')
	SpecialAttractions = models.TextField(default = 'null')

	def __str__(self):
		return self.Name

class TrainingApplicant(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CourseId = models.IntegerField(default=0)
	CourseName = models.CharField(default='null', max_length=50)
	Confirmed = models.BooleanField(default = False)
	Address = models.TextField(default='null')

	def __str__(self):
		return self.Name

class Client(models.Model):
	Name = models.CharField(max_length = 40)
	Email = models.EmailField(max_length = 70)
	Phone = models.BigIntegerField(default = 9898989898)
	CorpName = models.CharField(max_length = 100, default='null')
	Position = models.CharField(max_length = 100, default='null')
	Subject = models.TextField(default='null')

	def __str__(self):
		return self.Name
