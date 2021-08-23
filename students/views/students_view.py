from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from students.models.groups_model import Group
from students.models.students_model import Student

from datetime import datetime


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
    # if form was POST
    if request.method == "POST":

        # if form ADD button clicked
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}
            # data collection
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Імʼя є обовʼязковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обовʼязковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = "Дата народження є обовʼязковим"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = "Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = "Номер білета є обовʼязковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = "Оберіть групу для студента"
            else:
                group = Group.objects.filter(pk=student_group).first()
                if group:
                    data['student_group'] = group
                else:
                    errors['student_group'] = "Оберіть коректну групу"

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # create student object and save it to database
            if not errors:
                student = Student(**data)
                student.save()
                # redirect user to students list
                return HttpResponseRedirect(reverse('students:home'))

            # render form with errors and previous user input
            else:
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})

        # if form CANCEL button clicked
        elif request.POST.get('cancel_button') is not None:
            # redirect user to students list
            return HttpResponseRedirect(reverse('students:home'))

    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, student_id):
    return HttpResponse('<h1>Student Edit %s</h1>' % student_id)


def students_delete(request, student_id):
    return HttpResponse('<h1>Student Delete %s</h1>' % student_id)
