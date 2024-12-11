from django.shortcuts import render
from .models import Site
# Create your views here.

def home(request):
    obj = Site.objects.all()
    context={'obj':obj}
    return render(request,'index.html',context)