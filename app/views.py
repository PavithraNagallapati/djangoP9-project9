from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'harshad','age':32}
    return render(request,'conditions.html',context=d)