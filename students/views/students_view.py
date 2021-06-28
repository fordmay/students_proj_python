from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from students.models.students_model import Student
from students.models.groups_model import Group


def students_list(request):
    students = Student.objects.all()

    # try to order student list
    order_by = request.GET.get('order_by')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse') == '1':
            students = students.reverse()

    # paginator students
    paginator = Paginator(students, 3)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    # Якщо форма була запощена:
    
    #   Якщо кнопка Скасувати була натиснута:
    
    #       Повертаємо користувача до списку студентів
    
    #   Якщо кнопка Додати була натиснута:
    
    #       Перевіряємо данні на коректність та збираємо помилки
    
    #       Якщо данні були введені не коректно:
    #           Віддаємо шаблон форми разом із помилками
    
    #       Якщо данні були введені коректно:
    #           Створюємо та зберігаємо студента в базу
    
    #           Повертаємо користувача до списку студентів
    
    #       Якщо форма не була заповнена:
    #           Повертаємо код початкового стану форми
    
    
      
    groups = Group.objects.all().order_by('title')
    return render(request, 'students/students_add.html', {'groups': groups})


def students_edit(request, student_id):
    return HttpResponse('<h1>Student Edit %s</h1>' % student_id)


def students_delete(request, student_id):
    return HttpResponse('<h1>Student Delete %s</h1>' % student_id)
