from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
import json

def Home(request):
    # Data = Task.objects.all()
    # DataDictionary = {
    #             'Data' : Data 
    #         }
    return render(request, "JavaScript.html")
        
def NewTask(request):

    if (request.method == 'POST' and request.POST.get('Name') != "" and request.POST.get('Name').__eq__('N')):
            
        RealData = request.POST.get('Value')   

        NewTaskObeject = Task(Content = RealData)

        NewTaskObeject.save()

        ResponsedData = {"TaskId" :NewTaskObeject.id, "TaskData":NewTaskObeject.Content, 'TaskStatus': NewTaskObeject.Status}

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)

    elif (request.method == 'POST' and request.POST.get('Name') != "" and request.POST.get('Name').__eq__('C')):

        RealData = request.POST.get('Identity')   

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

    elif (request.method == 'POST' and request.POST.get('Name') != "" and request.POST.get('Name').__eq__('U')):

        SpecificTask = Task.objects.get(pk = request.POST.get('Identity'))

        SpecificTask.Content = request.POST.get('Value')

        SpecificTask.save()

        ResponsedData = {"TaskId" :request.POST.get('Identity'), "TaskNewContent":request.POST.get('Value')}

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)

    elif (request.method == 'GET' and request.GET.get('Name') != "" and request.GET.get('Name').__eq__('F')):

        ResponsedData = {}

        Data = Task.objects.all()

        for item in Data:
            
            ResponsedData[str(item)] = [item.id, item.Content, item.Status]

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)
            
    elif (request.method == 'POST' and request.POST.get('Name') != "" and request.POST.get('Name').__eq__('D')):

        RealData = request.POST.get('Identity')

        SpecificTask = Task.objects.get(pk = RealData)

        SpecificTask.delete()

        ResponsedData = {"TaskId" : RealData}

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)
        