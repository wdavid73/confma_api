from django.shortcuts import render


def HomePage(request, *args, **kwargs):
    return render(request, "index.html", {})
