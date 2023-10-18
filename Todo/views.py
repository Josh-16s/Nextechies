from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from .models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request , "task.html")
        else:
            return render(request , "Login.html" , {
                "message" : "invalid username or password"
            })

    return render(request , "Login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if confirm_password == password:
            user = User.objects.create_user( username = username, password = password)
            login (request , user)
            return render(request , 'Login.html')
        else:
            return render(request  , "register.html" , {
                "message": "Invalid password"
            })
    return render(request , "register.html")
 

def add(request):
     if request.method == 'POST':
        title = request.POST['task']
        task = Task(title=title, user=request.user)
        task.save()
        
        return redirect('view')  # Redirect to the page that displays the list of tasks
    
     return render(request, 'add.html')


def view(request):
    tasks = Task.objects.filter(user=request.user) 
    return render(request , "task.html" , {
        "tasks" : tasks
    })