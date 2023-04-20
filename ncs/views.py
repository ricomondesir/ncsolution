from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ncs/index.html")

def contact(request):
    return render(request, "ncs/contact.html")

def team(request):
    return render(request, "ncs/team.html")

def asanka(request):
    return render(request, "ncs/asanka.html")