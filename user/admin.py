from django.contrib import admin
from .models import User, ThreeFeaturedPic
# Register your models here.

class UserTable(admin.ModelAdmin):
    list_display= ('Name', 'Address', 'Email', 'Phone', 'Courses', 'id')
admin.site.register(User, UserTable)
class ThreeFeaturedPicTable(admin.ModelAdmin):
    list_display= ('Position', 'URLPointer', 'id') 
admin.site.register(ThreeFeaturedPic, ThreeFeaturedPicTable)
