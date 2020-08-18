from django.urls import path, include, re_path
from . import views
from django.views.generic import RedirectView
import re as r

urlpatterns = [
	path('', views.ResourcesMenuPg),
    re_path(r'pdf/$', views.PDFResourcesPg),
    re_path(r'jpg/$', views.JPGResourcesPg),
    re_path(r'ppt/$', views.PPTResourcesPg),
    re_path(r'aud/$', views.AUDResourcesPg),
    re_path(r'other/$', views.OtherResourcesPg),
    re_path(r'vid/$', views.VIDResourcesPg),
    ]	
