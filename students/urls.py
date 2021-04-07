"""Defines URL patterns for students."""
from django.urls import path
from . import views as stud_views

app_name = 'students'

urlpatterns = [
    # Students pages
    path('', stud_views.students_list, name='home'),
    path('students/add/', stud_views.students_add, name='students_add'),
    path('students/<int:student_id>/edit/', stud_views.students_edit, name='students_edit'),
    path('students/<int:student_id>/delete/', stud_views.students_delete, name='students_delete'),
    # Groups pages
    path('groups/', stud_views.groups_list, name='groups'),
    path('groups/add/', stud_views.groups_add, name='groups_add'),
    path('groups/<int:group_id>/edit/', stud_views.groups_edit, name='groups_edit'),
    path('groups/<int:group_id>/delete/', stud_views.groups_delete, name='groups_delete'),
]
