from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
import json

def Home(request):
    
    return render(request, "JavaScript.html")
        
def NewTask(request):

        if (request.method == 'POST' and request.POST.get('NewTask') != None):
                
            RealData = request.POST.get('NewTask')   

            NewObeject = Task(Content = RealData)

            NewObeject.save()

            ResponsedData = {"TaskId" :NewObeject.id, "TaskData":NewObeject.Content, 'TaskStatus': NewObeject.Status}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)

        elif (request.method == 'POST' and request.POST.get('Checked') != None):

            RealData = request.POST.get('Checked')   

            SpecificTask = Task.objects.get(pk = RealData)

            if SpecificTask.Status == 'true':

                SpecificTask.Status = 'false'

                SpecificTask.save()

                ResponsedData = {"TaskId" :RealData, "TaskStatus":'False'}

                Response = json.dumps(ResponsedData)

                return HttpResponse(Response)

            else:

                SpecificTask.Status = 'true'

                SpecificTask.save()

                ResponsedData = {"TaskId" :RealData, "TaskStatus":'True'}

                Response = json.dumps(ResponsedData)

                return HttpResponse(Response) 

        elif (request.method == 'POST' and request.POST.get('Update') != None):

            SpecificTask = Task.objects.get(pk = request.POST.get('Update'))

            SpecificTask.Content = request.POST.get('Value')

            SpecificTask.save()

            ResponsedData = {"TaskId" :request.POST.get('Update'), "TaskNewContent":request.POST.get('Value')}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)

        elif (request.method == 'GET' and request.GET.get('StartLoad') != ""):

            ResponsedData = {}

            Data = Task.objects.all()

            for item in Data:
                
                ResponsedData[str(item)] = [item.id, item.Content, item.Status]

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)
                
        elif (request.method == 'POST' and request.POST.get('Delete') != None):

            RealData = request.POST.get('Delete')

            SpecificTask = Task.objects.get(pk = RealData)

            SpecificTask.delete()

            ResponsedData = {"TaskId" : RealData}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)
            