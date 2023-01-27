from django.shortcuts import render

# Create your views here.

def tareas(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')   
def deber(request):
    return render(request, 'tareas.html') 
def recursos(request):
    return render(request, 'recursos.html') 



    