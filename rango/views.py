from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    html = "<a href='/rango/about/'>About</a>"
    return HttpResponse(f"Rango says hey there partner!{html}")
    #return render(request, html)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
