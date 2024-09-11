from django.shortcuts import render


def home(request):
    return render(request, "on_tap/base.html")
