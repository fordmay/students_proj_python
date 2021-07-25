from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
    # if form was POST
    if request.method == "POST":

        # if form ADD button clicked
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            # check data for corrections and errors
            errors = {}

            # if data was correct
            if not errors:
                # create student object and save it to database
                student = Student(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    birthday=request.POST['birthday'],
                    photo=request.FILES['photo'],
                    ticket=request.POST['ticket'],
                    student_group=Group.objects.get(pk=request.POST['student_group']),
                    notes=request.POST['notes']
                )
                student.save()
                # redirect user to students list
                return HttpResponseRedirect(reverse('students:home'))

            # if data wasn't correct
            else:
                # render form with errors and previous user input
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
