from django.http import HttpResponse
from django.shortcuts import render


def journal_list(request):
    return HttpResponse('<h1>Journal List</h1>')
