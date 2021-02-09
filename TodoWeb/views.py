from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
import json

def Home(request):
    Data = Task.objects.all()
    DataDictionary = {
                'Data' : Data 
            }
    return render(request,'JavaScript.html', DataDictionary)

def NewTask(request, UrlValue):
    if request.method == 'POST':
        if(UrlValue != ""):
            
            IdentifyUrl = UrlValue

            if (IdentifyUrl[0] == 'N'):
                    
                RealData = IdentifyUrl[2:]   

                NewTaskObeject = Task(Content = RealData)

                NewTaskObeject.save()
  
                ResponsedData = {"TaskId" :NewTaskObeject.id, "TaskData":NewTaskObeject.Content}

                Response = json.dumps(ResponsedData)
     
                return HttpResponse(Response)

            elif (IdentifyUrl[0] == 'C'):

                RealData = IdentifyUrl[2:]  

                TaskCompleteIdentity = int(RealData) 

                SpecificTask = Task.objects.get(pk = TaskCompleteIdentity)

                if SpecificTask.Status == 'true':

                    SpecificTask.Status = 'false'

                    SpecificTask.save()

                    TaskCompleteIdentity = str(TaskCompleteIdentity)

                    ResponsedData = {"TaskId" :TaskCompleteIdentity, "TaskStatus":'False'}

                    Response = json.dumps(ResponsedData)
     
                    return HttpResponse(Response)

                else:

                    SpecificTask.Status = 'true'

                    SpecificTask.save()

                    TaskCompleteIdentity = str(TaskCompleteIdentity)

                    ResponsedData = {"TaskId" :TaskCompleteIdentity, "TaskStatus":'True'}

                    Response = json.dumps(ResponsedData)
     
                    return HttpResponse(Response) 

            elif (IdentifyUrl[0] == 'U'):

                RealData = IdentifyUrl[2:]

                DataList = RealData.split("-") 

                SpecificTask = Task.objects.get(pk = int(DataList[0]))

                SpecificTask.Content = DataList[1]

                SpecificTask.save()

                ResponsedData = {"TaskId" :DataList[0], "TaskNewContent":DataList[1]}

                Response = json.dumps(ResponsedData)
     
                return HttpResponse(Response)

            else:

                RealData = IdentifyUrl[2:]

                SpecificTask = Task.objects.get(pk = int(RealData))

                SpecificTask.delete()

                ResponsedData = {"TaskId" : RealData}

                Response = json.dumps(ResponsedData)
     
                return HttpResponse(Response)
                