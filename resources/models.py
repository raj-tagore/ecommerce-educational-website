from django.db import models

# Create your models here.
class PDFResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name

class JPGResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name

class PPTResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name

class AUDResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name

class VIDResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name

class OtherResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')

	def __str__(self):
		return self.Name
