from django.http import HttpResponse
from django.shortcuts import render
from students.models import Group


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, group_id):
    return HttpResponse('<h1>Group Edit %s</h1>' % group_id)


def groups_delete(request, group_id):
    return HttpResponse('<h1>Group Delete %s</h1>' % group_id)
