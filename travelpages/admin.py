from django.contrib import admin

# Register your models here.
from .models import Student, Grade_level

admin.site.register(Student)
admin.site.register(Grade_level)