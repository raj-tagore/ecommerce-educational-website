from django.shortcuts import render
import os
from .models import JPGResource, PDFResource, PPTResource, OtherResource, AUDResource, VIDResource
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "https://rtwebsitebucket.s3.us-east-1.amazonaws.com/"

def ResourcesMenuPg(request):
	return render(request, 'resourcesmenu.html', {'Media' : MEDIA_URL})

def JPGResourcesPg(request):
	AllResourcesObj = JPGResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})

def PDFResourcesPg(request):
	AllResourcesObj = PDFResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})
  
def PPTResourcesPg(request):
	AllResourcesObj = PPTResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})

def OtherResourcesPg(request):
	AllResourcesObj = OtherResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})

def AUDResourcesPg(request):
	AllResourcesObj = AUDResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})

def VIDResourcesPg(request):
	AllResourcesObj = VIDResource.objects.all()
	return render(request, 'resources.html', {'Product' : AllResourcesObj, 'Media' : MEDIA_URL})