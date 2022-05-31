from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'BlogApp/index.html')

def citation_view(request):
    return render(request, 'BlogApp/citation_page.html')

def contact_view(request):
    return render(request, 'BlogApp/contact_view.html')