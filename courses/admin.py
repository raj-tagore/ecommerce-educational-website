from django.contrib import admin
from .models import Course, CourseApplicant


# Register your models here.
class CourseTable(admin.ModelAdmin):
    list_display= ('id', 'Name', 'Price')
admin.site.register(Course, CourseTable)

class CourseApplicantTable(admin.ModelAdmin):
    list_display= ('id', 'Name', 'CourseName', 'Email', 'Phone')
admin.site.register(CourseApplicant, CourseApplicantTable)
