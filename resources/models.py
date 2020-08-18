from django.db import models

# Create your models here.
class PDFResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')

class JPGResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')

class PPTResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
    File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')

class AUDResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
    File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')

class VIDResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
    File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')

class OtherResource(models.Model):
	Name = models.CharField(max_length = 150)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
    File = models.FileField(upload_to = 'Resources/ResourceFiles/', default = 'null')
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')