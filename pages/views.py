from django.shortcuts import render

# Create your views here.
def HomeIndex(request):
    return render(request, 'pages/pages/home.html')