from django.contrib import admin
from .models import TrainingProgram, TrainingApplicant,TrainingApplicantType, TrainingCategory


# Register your models here.
admin.site.register(TrainingProgram)
admin.site.register(TrainingApplicant)
