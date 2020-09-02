from django.contrib import admin
from .models import VIDResource, PDFResource, AUDResource, PPTResource, JPGResource, OtherResource    

# Register your models here.
admin.site.register(PDFResource)
admin.site.register(PPTResource)
admin.site.register(JPGResource)
admin.site.register(VIDResource)
admin.site.register(AUDResource)
admin.site.register(OtherResource)