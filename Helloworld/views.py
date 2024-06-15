from django.shortcuts import HttpResponse, render


def index(request):
    #return render(request, 'index.html')
    return HttpResponse("Hello, Django")

def about(request):
    return render(request, 'about.html')