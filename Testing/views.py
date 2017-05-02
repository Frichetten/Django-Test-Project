from django.shortcuts import render


def home(request):
    context = {'data': 'Passing information to the front end'}
    return render(request, "home.html", context)
