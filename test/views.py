from django.shortcuts import render
from django.http import HttpResponse


def test_start(request):
    return render(request, "start.html")
