from django.shortcuts import render, HttpResponse, redirect
from django.urls import path, include
from app.models import Posts

# Create your views here.
def home(request):
    post = Posts.objects.all()
    return render(request,'index.html', {'post':post})


def detail(request, id):
    post = Posts.objects.get(id= id)
    return render(request, 'detail.html',{'post':post})

def add(request):
    return render(request, 'create.html')

def addrec(request):
    n = request.POST['user_name']
    c = request.POST['content']
    post = Posts(
        user_name= n,
        content= c
        )
    post.save()
    return redirect('home')

def update(request, id):
    post = Posts.objects.get(id = id)
    return render(request, 'edit.html', {'post':post})

def uprec(request, id):
    n = request.POST['user_name']
    c = request.POST['content']
    post = Posts.objects.get(id = id)
    post.user_name = n
    post.content = c

    post.save()
    return redirect('home')

def delete(request, id):
    post = Posts.objects.get(id = id)
    post.delete()
    return redirect('home')

