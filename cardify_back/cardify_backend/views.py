from django.shortcuts import render

# Create your views here.

def cardify_view(request):
    return render(request, 'cardify_backend.html', {})