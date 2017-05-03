from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Testing.models import File
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def home(request):
    if request.user.is_authenticated():
        context = {'data': 'You are logged in ' + request.user.username}
    else:
        context = {'data': 'You are not logged in'}
    return render(request, "home.html", context)


def test(request):
    if request.method != "POST":
        return HttpResponse("<h1>Fail</h1>")
    file = File(name=request.POST.get("name"), description=request.POST.get("description"))
    file.save()
    return HttpResponseRedirect("/")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')
