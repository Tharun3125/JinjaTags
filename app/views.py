from django.shortcuts import render

# Create your views here.


def condition(request):
    d={'name':'Tharun','age':23}
    return render(request,'jinja.html',d)

def loops(request):
    d={'CDT':[10,20,30,40,50]}
    return render(request,'jinja_loop.html',d)
