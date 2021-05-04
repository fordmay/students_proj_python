from django.http import HttpResponse
from django.shortcuts import render


def journal_list(request):
    journals = (
        {'student': {'id': 1, 'name': 'Мейсон Пайнс'}},
        {'student': {'id': 2, 'name': 'Майбл Пайнс'}},
        {'student': {'id': 3, 'name': 'Стенлі Пайнс'}}
    )
    return render(request, 'students/journal_list.html', {'journals': journals})
