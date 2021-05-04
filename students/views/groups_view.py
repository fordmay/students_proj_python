from django.http import HttpResponse
from django.shortcuts import render


def groups_list(request):
    groups = (
        {'id': 1,
         'name': 'ME-1',
         'leader': {'id': 1, 'name': 'Мейсон Пайнс'}},
        {'id': 2,
         'name': 'ME-2',
         'leader': {'id': 2, 'name': 'Майбл Пайнс'}},
        {'id': 3,
         'name': 'ME-3',
         'leader': {'id': 3, 'name': 'Стенлі Пайнс'}}
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, group_id):
    return HttpResponse('<h1>Group Edit %s</h1>' % group_id)


def groups_delete(request, group_id):
    return HttpResponse('<h1>Group Delete %s</h1>' % group_id)
