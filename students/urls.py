"""Defines URL patterns for students."""
from django.urls import path
from students.views import students_view, groups_view, journal_view

app_name = 'students'

urlpatterns = [
    # Students pages
    path('', students_view.students_list, name='home'),
    path('students/add/', students_view.students_add, name='students_add'),
    path('students/<int:student_id>/edit/', students_view.students_edit, name='students_edit'),
    path('students/<int:student_id>/delete/', students_view.students_delete, name='students_delete'),
    # Groups pages
    path('groups/', groups_view.groups_list, name='groups'),
    path('groups/add/', groups_view.groups_add, name='groups_add'),
    path('groups/<int:group_id>/edit/', groups_view.groups_edit, name='groups_edit'),
    path('groups/<int:group_id>/delete/', groups_view.groups_delete, name='groups_delete'),
    # Journal pages
    path('journal/', journal_view.journal_list, name='journal')
]
