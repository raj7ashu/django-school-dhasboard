from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def adminclick_view(request):
    return render(request,'adminclick.html')

def studentclick_view(request):
    return render(request,'studentclick.html')

def teacherclick_view(request):
    return render(request,'teacherclick.html')
