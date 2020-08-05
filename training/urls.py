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
    re_path(r'TPaymentFailure', views.TPaymentFailure)
]