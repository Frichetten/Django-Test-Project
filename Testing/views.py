from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Testing.models import File


def home(request):
    if request.user.is_authenticated():
        context = {'data': 'You are logged in ' + request.user.username}
    else:
        context = {'data': 'You are not logged in'}
    file = File.objects.all()
    print(file.values_list())
    return render(request, "home.html", context)


def test(request):
    if request.method != "POST":
        return HttpResponse("<h1>Fail</h1>")
    file = File(name=request.POST.get("name"), description=request.POST.get("description"))
    file.save()
    return HttpResponseRedirect("/")

