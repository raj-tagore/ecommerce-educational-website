from django.urls import path, include, re_path
from . import views
from django.views.generic import RedirectView
import re as r

urlpatterns = [
    path(r'', views.HomeView),
    re_path(r'index$', views.HomeView),
    re_path(r'login/$', views.LoginView),
    re_path(r'register/$', views.RegisterView),
    re_path(r'register$', views.RegisterView),
    re_path(r'verify$', views.Verify),
    re_path(r'logout$', views.Logout),
    re_path(r'addInfo$', views.AddUserInfo),
    re_path(r'about/$', views.AboutView),
    re_path(r'contact/$', views.ContactView),
    re_path(r'purchased/$', views.ProductsView) 
]