from django.shortcuts import render

def welcome(request):
    return render(request, 'landing/index.html')
