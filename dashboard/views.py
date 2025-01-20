# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Dashboard Home")
from django.shortcuts import render

# Define the 'index' view
def index(request):
    return render(request, 'dashboard/index.html')
