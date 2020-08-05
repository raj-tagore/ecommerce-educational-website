from django.urls import path, include, re_path
from . import views
from django.views.generic import RedirectView
import re as r

urlpatterns = [
	path('', views.ProductsPg),
	#path('searchCoursesbyname/specificCourse/<namo>/', views.SpecificCoursePg),
    #re_path(r'searchCourses/$', views.searchCourses),
    re_path(r'SearchProducts/$', views.SearchProducts),
    path('ViewProduct/<ProductId>/', views.ViewProduct),
    re_path(r'Pay1/$', views.Pay1),
    re_path(r'Pay2/$', views.Pay2),
    re_path(r'PPaymentSuccess/', views.PaymentSuccess),
    re_path(r'PPaymentFailure/', views.PaymentFailure)
    ]	
