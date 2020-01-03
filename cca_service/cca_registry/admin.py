from django.contrib import admin
from .models.student import Student
from .models.school import School


admin.site.register(Student)
admin.site.register(School)
