from django.contrib import admin
from .models.students_model import Student
from .models.groups_model import Group


admin.site.register(Student)
admin.site.register(Group)
