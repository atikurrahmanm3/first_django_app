from django.shortcuts import render
from .models import aboutus
# Create your views here.


def home(request):

    return render(request, "index.html")


def about(request):
    aboutdata = aboutus.objects.all()[0]
    context = {
        'aboutus': aboutdata
    }

    return render(request, "about.html", context)


def blogs(request):
    return render(request, "blogs.html")
