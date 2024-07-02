from django.shortcuts import render , redirect
from django.http import HttpRequest
from home.models import Tasks

# Create your views here.
def home(request):
    context ={'success': False}
    if request.method == "POST":
        #handle the form 
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Tasks(taskTitle= title , taskDesc = desc)
        ins.save()
        context = {'success' : True }
    return render(request,'index.html', context)

def create_task(request):
    if request.method == 'POST':
        task_title = request.POST['taskTitle']
        task_desc = request.POST['taskDesc']
        task = Tasks(taskTitle=task_title, taskDesc=task_desc, approved=False)
        task.save()
        return redirect('tasks')  # Redirect to the tasks list page
    return render(request, 'tasks.html')  # Render the tasks list page

def tasks(request):
    allTasks = Tasks.objects.filter(approved=True)  # Only show approved tasks
    context = { 'tasks': allTasks}
    return render(request,'tasks.html',context)
    

        