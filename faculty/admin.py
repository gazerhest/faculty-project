from django.contrib import admin
from .models import FacultyInfo, Department, Program, Teacher, ExchangeProgram

class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'dean', 'phone', 'email']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'boss']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'department', 'coordinator_name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'degree', 'department']


class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ['university_name', 'country', 'languages', 'slots', 'deadline']

admin.site.register(FacultyInfo, FacultyInfoAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ExchangeProgram, ExchangeProgramAdmin)
