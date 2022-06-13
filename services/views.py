from unicodedata import name
from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request,'service.html')
def skills(request):
    return render(request,'skills.html')
def mskills(request):
    return render(request,'mskills.html')