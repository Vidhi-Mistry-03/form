from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect,HttpResponse

def home(request):
    # return HttpResponse('hii! i am working')
    return render(request,'form.html')
    