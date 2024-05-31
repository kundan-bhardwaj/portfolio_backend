from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(service)
admin.site.register(serviceattribute)
admin.site.register(technology)
admin.site.register(skill)
admin.site.register(project)
# admin.site.register(order)
admin.site.register(doc)
admin.site.register(social)
admin.site.register(education)