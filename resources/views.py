from django.shortcuts import render
import os
from .models import JPGResource, PDFResource, PPTResource, OtherResource, AUDResource, VIDResource
from ..RTwebsite import settings

BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL

def ResourcesMenuPg(request):
	return render(request, 'resourcesmenu.html', {'Media' : MEDIA_URL})

def JPGResourcesPg(request):
	AllResourcesObj = JPGResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})

def PDFResourcesPg(request):
	AllResourcesObj = PDFResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})
  
def PPTResourcesPg(request):
	AllResourcesObj = PPTResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})

def OtherResourcesPg(request):
	AllResourcesObj = OtherResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})

def AUDResourcesPg(request):
	AllResourcesObj = AUDResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})

def VIDResourcesPg(request):
	AllResourcesObj = VIDResource.objects.all()
	return render(request, 'resources.html', {'Resource' : AllResourcesObj, 'Media' : MEDIA_URL})