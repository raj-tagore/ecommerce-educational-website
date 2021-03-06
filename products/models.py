from django.db import models

# Create your models here.
class Product(models.Model):
	Name = models.CharField(max_length = 100)
	Brief = models.CharField(max_length = 200, default='Max 200 characters')
	About = models.TextField(default = 'null')
	BasePrice = models.IntegerField(default = 0)
	DeliveryCharges = models.IntegerField(default = 0)
	Price = models.IntegerField(default = 0)
	ActivateDiscount = models.BooleanField(default = False)
	DiscountedPrice = models.IntegerField(default = 0)
	FrontPic = models.ImageField(upload_to = 'Products/FrontPics/', default = 'null')
	Tags = models.TextField(default = 'null')
	Display = models.BooleanField(default = True)
	Position = models.IntegerField(default=1)
	DaysForDelivery = models.IntegerField(default=8)
	ShowDealer = models.BooleanField(default = False)
 
	def __str__(self):
		return self.Name

class Buyer(models.Model):
	Name = models.CharField(max_length = 50)
	Address = models.TextField(default = 'null')
	Phone = models.BigIntegerField(default = 9898989898)
	Email = models.EmailField(default = 'null')
	ProductId = models.IntegerField(default = 0)
	ProductName = models.CharField(max_length = 100)
	Dealer = models.CharField(max_length = 200, default='null')

	def __str__(self):
		return self.Name
