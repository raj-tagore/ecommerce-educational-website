from django.urls import path, include, re_path
from . import views
from django.views.generic import RedirectView
import re as r

urlpatterns = [
	path('', views.CourseListView),
	path('index/', views.HomeView),
	path('CourseList/', views.CourseListView),
	path('SpecificCourse/<namo>/', views.SpecificCourseView),
	path('login/purchased/coursesList/SpecificCourse/<namo>/', views.SpecificCourseView),
	path('SearchCourse/SpecificCourse/<namo>/', views.SpecificCourseView),
	path('SearchCourseByName/SpecificCourse/<namo>/', views.SpecificCourseView),
	re_path(r'SearchCourse/$', views.SearchCourse),
	re_path(r'SpecificCourse/$', views.RedirectView),
	re_path(r'SearchCourseByName/$', views.SearchCourseByName),
	path('pay1/<CourseId>/', views.Pay1),
	path(r'pay1/<CourseId2>/pay2/', views.Pay2),
	re_path(r'pay3payU/', views.Pay3PayU), 
	re_path('PaymentSuccess/', views.PaymentSuccess),
	re_path('PaymentFailure/', views.PaymentFailure)
]