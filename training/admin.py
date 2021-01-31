from django.contrib import admin
from .models import TrainingProgram, TrainingApplicant,TrainingApplicantType, TrainingCategory


# Register your models here.
class TrainingTable(admin.ModelAdmin):
    list_display= ('Name', 'Price', 'Position', 'Dates', 'Display', 'Language', 'id')
admin.site.register(TrainingProgram, TrainingTable)
class TrainingApplicantTable(admin.ModelAdmin):
    list_display= ('Name', 'id', 'Phone', 'CourseName', 'Email')
admin.site.register(TrainingApplicant, TrainingApplicantTable)
