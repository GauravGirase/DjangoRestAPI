from django.contrib import admin

from .models import School, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "pin_code", "email", "password", "created_by")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "password", "grade", "school", "created_by")


