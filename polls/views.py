from django.http import HttpResponse
def homepage(request):
    return HttpResponse('<h1>Hello <span style="color:red">Django</span></h1>')