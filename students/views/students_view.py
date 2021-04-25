from django.http import HttpResponse
from django.shortcuts import render


def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Мейсон',
         'last_name': 'Пайнс',
         'ticket': 215,
         'image': 'img/gravity_falls_na_avu01.jpg'},
        {'id': 2,
         'first_name': 'Мейбл',
         'last_name': 'Пайнс',
         'ticket': 152,
         'image': 'img/gravity_falls_na_avu02.jpg'},
        {'id': 3,
         'first_name': 'Стенлі',
         'last_name': 'Пайнс',
         'ticket': 64,
         'image': 'img/gravity_falls_na_avu03.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, student_id):
    return HttpResponse('<h1>Student Edit %s</h1>' % student_id)


def students_delete(request, student_id):
    return HttpResponse('<h1>Student Delete %s</h1>' % student_id)
