from django.contrib import admin
from .models import OnlineTrainingProgram, OnlineTrainingApplicant, OnlineTrainingApplicantType, OnlineTrainingCategory


# Register your models here.
admin.site.register(OnlineTrainingProgram)
admin.site.register(OnlineTrainingApplicant)
admin.site.register(OnlineTrainingCategory)
admin.site.register(OnlineTrainingApplicantType)
