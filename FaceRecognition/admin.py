from django.contrib import admin

# Register your models here.
from .models import admindata, student, department, sec

admin.site.register(admindata)
admin.site.register(student)
admin.site.register(department)
admin.site.register(sec)
