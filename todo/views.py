from turtle import title
from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todo = Todo.objects.all()
    if(request.method == 'POST'):
        new_todo = Todo(
            title=request.POST["title"]
        )
        if(new_todo.title !=""):
            new_todo.save()
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'index.html', {'todos': todo})


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")
