from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'page':'Om Chaudhari'
    }
    return render(request,'home.html',context)

def about(request):
    context = {
        'page':'About'
    }
    return render(request,'about.html',context)

def skills(request):
    context = {
        'page':'Skills'
    }
    return render(request,'skills.html',context)

def projects(request):
    context = {
        'page':'Projects'
    }
    return render(request,'projects.html',context)

def link(request):
    context = {
        'page':'Links'
    }
    return render(request,'link.html',context)
