from django.shortcuts import render

def customize_shoe(request):
    return render(request, 'customizer/index.html')