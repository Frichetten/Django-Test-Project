from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        context = {'data': 'You are logged in ' + request.user.username}
    else:
        context = {'data': 'You are not logged in'}
    return render(request, "home.html", context)
