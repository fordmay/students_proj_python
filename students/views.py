from django.http import HttpResponse
from django.shortcuts import render


# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Ім’я-1',
         'last_name': 'Перший',
         'ticket': 215,
         'image': 'img/gravity_falls_na_avu02.jpg'},
        {'id': 2,
         'first_name': 'Ім’я-2',
         'last_name': 'Другий',
         'ticket': 152,
         'image': 'img/gravity_falls_na_avu04.jpg'},
        {'id': 3,
         'first_name': 'Ім’я-3',
         'last_name': 'Третій',
         'ticket': 64,
         'image': 'img/gravity_falls_na_avu05.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, student_id):
    return HttpResponse('<h1>Student Edit %s</h1>' % student_id)


def students_delete(request, student_id):
    return HttpResponse('<h1>Student Delete %s</h1>' % student_id)


# Views for Groups
def groups_list(request):
    return HttpResponse('<h1>Groups List</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, group_id):
    return HttpResponse('<h1>Group Edit %s</h1>' % group_id)


def groups_delete(request, group_id):
    return HttpResponse('<h1>Group Delete %s</h1>' % group_id)
