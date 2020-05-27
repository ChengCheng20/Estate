from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def agentsingle(request):
    return render(request, 'agentsingle.html', {})

def agentgrid(request):
    return render(request, 'agentgrid.html', {})

def blogsingle(request):
    return render(request, 'blogsingle.html', {})

def bloggrid(request):
    return render(request, 'bloggrid.html', {})

def propertysingle(request):
    return render(request, 'propertysingle.html', {})

def propertygrid(request):
    return render(request, 'propertygrid.html', {})
