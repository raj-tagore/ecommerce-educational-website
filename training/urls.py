from django.urls import path, include, re_path
from . import views
from django.views.generic import RedirectView
import re as r

urlpatterns = [
    path('', views.TrainingPg),
    re_path(r'training/$', views.TrainingPg),
    re_path(r'host/$', views.HostTrainingPg), 
    path(r'ApplyFor/<CourseName>/', views.ApplyForTraining),
    #re_path(r'AddParticipantForTraining/$', views.SaveDataOfApplicant),
    #re_path(r'AddClient/$', views.AddClient),
    re_path(r'pay2/$', views.Pay2),
    re_path(r'pay3TpayU/$', views.Pay3),
    re_path(r'TPaymentSuccess', views.TPaymentSuccess),
    re_path(r'TPaymentFailure', views.TPaymentFailure),
    re_path(r'Insurance/$', views.InsuranceTrainingPg),
    re_path(r'Sales/$', views.SalesTrainingPg),
    re_path(r'NetworkMarketing/$', views.NetworkMarketingTrainingPg),
    re_path(r'Business/$', views.BusinessTrainingPg),
    re_path(r'SelfDevelopment/$', views.SelfDevelopmentTrainingPg),
    path(r'ReadMore/<CourseName>/', views.MoreAboutTraining),  
]