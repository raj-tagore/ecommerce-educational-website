from django.contrib import admin
from .models import OnlineTrainingProgram, OnlineTrainingApplicant, OnlineTrainingApplicantType, OnlineTrainingCategory


# Register your models here.
class OnlineTrainingTable(admin.ModelAdmin):
    list_display= ('Name', 'Price', 'Position', 'Dates', 'Display', 'Language', 'id')
admin.site.register(OnlineTrainingProgram, OnlineTrainingTable)
class OnlineTrainingApplicantTable(admin.ModelAdmin):
    list_display= ('Name', 'CourseName', 'Email', 'Phone', 'id')
admin.site.register(OnlineTrainingApplicant, OnlineTrainingApplicantTable)
