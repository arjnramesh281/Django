from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return HttpResponse("Django!")

l=[]
def fun(req):
    if req.method=="POST":
        name=req.POST["name"]
        age=req.POST["age"]
        l.append({"name":name,"age":age})
        print(l)
        return redirect(fun)
    else:
        return render(req,"demo.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


l=[{"name":"akhil", "age": "21"},{"name":"don","age":"32"}]

def display(req):
    return render(req,"display.html",{"data":l})


def add(req):
    if req.method=="POST":
        name=req.POST["name"]
        age=req.POST["age"]
        l.append({"name":name,"age":age})
        return redirect(display)
    else:
        return render(req,"add.html")