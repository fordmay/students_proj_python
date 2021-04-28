from django.http import HttpResponse
from django.shortcuts import render


def journal_list(request):
    return render(request, 'students/journal_list.html')
