from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def Home(request):
    Data = Task.objects.all()
    DataDictionary = {
                'Data' : Data 
            }
    return render(request,'JavaScript.html', DataDictionary)

def NewTask(request):
    if request.method == 'POST':
        TaskContent = request.POST.get('TaskContent')
        if(TaskContent != ""):
            NewTaskObeject = Task(Content = TaskContent)
            NewTaskObeject.save()
            Data = Task.objects.all()
            DataDictionary = {
                        'Data' :Data 
                    } 
            return redirect('Home')
        else:
            TaskContent = request.POST.get('TaskContent')
            Data = Task.objects.all()
            DataDictionary = {
                        'Data' : Data 
                    } 
            return redirect('Home')
def StatusChange(request, id):
    SpecificTask = Task.objects.get(pk = id)
    if SpecificTask.Status == 'true':
        SpecificTask.Status = 'false'
        SpecificTask.save()
        return redirect('Home')
    else:
        SpecificTask.Status = 'true'
        SpecificTask.save()
        return redirect('Home')  

def TaskEdit(request, id, ChangedContent):
    SpecificTask = Task.objects.get(pk = id)
    SpecificTask.Content = ChangedContent
    SpecificTask.save()
    return redirect('Home')
       
def TaskDelete(request, id):
    SpecificTask = Task.objects.get(pk = id)
    SpecificTask.delete()
    return redirect('Home')
        



