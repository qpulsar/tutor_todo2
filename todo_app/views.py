from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'todo_app/index.html')


def about(request):
    return render(request, 'todo_app/about.html');


def create(request):
    return render(request, 'todo_app/create.html');
