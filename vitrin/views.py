from django.shortcuts import render, HttpResponse


def index(request:object) -> HttpResponse:
    """Index page of the flighty website"""
    return HttpResponse('<div align="center"><h1>Welcome to the flighty!</h1></div>')
