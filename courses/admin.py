from django.contrib import admin
from .models import Course, CourseApplicant


# Register your models here.
class CourseTable(admin.ModelAdmin):
    list_display= ('Name', 'Price', 'id')
admin.site.register(Course, CourseTable)

class CourseApplicantTable(admin.ModelAdmin):
    list_display= ('Name', 'CourseName', 'Email', 'Phone', 'id')
admin.site.register(CourseApplicant, CourseApplicantTable)
