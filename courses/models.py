from django.db import models
import os

# Create your models here.
class Course(models.Model):

	Name = models.CharField(max_length = 50)
	About = models.TextField(default = 'null')
	Price = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'courses/frontpics/', default = 'null')
	Tags = models.TextField(default = 'null')
	videofile1 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile2 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile3 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile4 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile5 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile6 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile7 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile8 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile9 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile10 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile11 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile12 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile13 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile14 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile15 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile16 = models.FileField(upload_to='courses/videos/', null=True, default = 'null') 
	videofile17 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile18 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile19 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile20 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile21 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile22 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile23 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile24 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile25 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile26 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile27 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile28 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile29 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')
	videofile30 = models.FileField(upload_to='courses/videos/', null=True, default = 'null')


	
