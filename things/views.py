from django.shortcuts import render

def things_view(request):
    return render(request, 'things/homepage.html')
# Create your views here.
