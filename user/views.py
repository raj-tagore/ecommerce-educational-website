from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.shortcuts import HttpResponse
from .models import ThreeFeaturedPic
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

# Create your views here.
def HomeView(request):
	ShowFeatured = True
	FeaturedObj = ThreeFeaturedPic.objects.all()
	FeaturedObj = sorted(FeaturedObj, key=lambda ThreeFeaturedPic: ThreeFeaturedPic.Position)
	Featured1 = FeaturedObj[0]
	Featured2 = FeaturedObj[1]
	Featured3 = FeaturedObj[2]
	VarDict = {'Featured1': Featured1, 'Featured2': Featured2, 'Featured3': Featured3, 'ShowFeatured': ShowFeatured, 'Media': MEDIA_URL}
	return render(request, 'index.html', VarDict)

def LoginView(request):
	Prompt = "Login to continue"
	return render(request, 'login.html', {'Prompt' : Prompt})

def RegisterView(request):
	return render(request, 'regs.html')

def AddUserInfo(request):
	Name = request.POST["Name"]
	Email = request.POST["Email"]
	Password = request.POST["Password"]
	Phone = request.POST["Phone"]
	Address = request.POST["Address1"]+", "+request.POST["Address2"]+", "+request.POST["Address3"]+", "+request.POST["PinCode"]
	Persons = User.objects.all()
	Exists = False 
	for i in Persons:
		if(i.Email == Email):
			Prompt = "This Email is registered to another account"
			Exists = True
		else:
			continue
	for i in Persons:
		if(i.Phone == Phone):
			Prompt = "Phone number is registered to another account"
			Exists = True
		else:
			continue
	if(Exists):
		return render(request, 'regs.html', {'Prompt': Prompt})
	else: 
		NewUser = User()
		NewUser.Name = Name
		NewUser.Address = Address
		NewUser.Email = Email
		NewUser.Password = Password
		NewUser.Phone = Phone
		NewUser.Premium = False
		NewUser.save()
		return render(request, 'index.html')



def Verify(request):
	Email = request.POST["Email"]
	Password = request.POST["Password"]
	Verified = False
	Prompt = "Error, Wrong credentials"
	Persons = User.objects.all()
	for i in Persons:
		print(i.Email)
		if (i.Email == Email):
			if (i.Password == Password):
				Verified = True
				return render(request, 'index.html', {'Verified' :  Verified, 'User' : i})
			else:
				Prompt = "Wrong Password"
				return render(request, 'login.html', {'Prompt' : Prompt})
		else:
			Prompt = "User Doesnt Exist"
			continue
	return render(request, 'login.html', {'Prompt' : Prompt})

def Logout(request):
	return render(request, 'index.html')

def Error(request):
	return HttpResponse('We encountered an error. Please return to the homepage')


def AboutView(request):
	return render(request, 'about.html')

def ContactView(request):
	return render(request, 'contact.html')

def ProductsView(request):
	UId = request.POST["UId"]
	UserObj = User.objects.get(id = int(UId))
	Courses = UserObj.Courses.all()
	return render(request, 'userproducts.html', {'User' : UserObj, 'Courses' : Courses, 'Media' : MEDIA_URL})

