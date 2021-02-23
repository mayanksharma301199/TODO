from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task, User
import json
import time
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

def Home(request):
    
    return render(request, "LogInJs.html")

def UserHome(request):

    return render(request, "JavaScript.html")
     
def NewTask(request):

    if request.method == 'POST':

        try:

            decodedToken = JwtTokenDecode(request.headers.get("Authorization"))

        except:

            return HttpResponse("Time Out!")

        if (request.POST.get('NewTask') != None):

            RealData = request.POST.get('NewTask')   

            NewObeject = Task(Content = RealData, Userid = decodedToken["user_id"])

            NewObeject.save()

            ResponsedData = {"TaskId" :NewObeject.id, "TaskData":NewObeject.Content, 'TaskStatus': NewObeject.Status}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)

        elif (request.POST.get('Checked') != None):

            RealData = request.POST.get('Checked')   

            SpecificTask = Task.objects.get(pk = RealData, Userid = decodedToken["user_id"])

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

        elif (request.POST.get('Update') != None):

            SpecificTask = Task.objects.get(pk = request.POST.get('Update') , Userid = decodedToken["user_id"])

            SpecificTask.Content = request.POST.get('Value')

            SpecificTask.save()

            ResponsedData = {"TaskId" :request.POST.get('Update'), "TaskNewContent":request.POST.get('Value')}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)
                
        elif (request.POST.get('Delete') != None):

            RealData = request.POST.get('Delete')

            SpecificTask = Task.objects.get(pk = RealData, Userid = decodedToken["user_id"])

            SpecificTask.delete()

            ResponsedData = {"TaskId" : RealData}

            Response = json.dumps(ResponsedData)

            return HttpResponse(Response)

    else:

        try:

            decodedToken = JwtTokenDecode(request.headers.get("Authorization"))

        except:

            return HttpResponse("Time Out!")

        ResponsedData = {}

        Data = Task.objects.all()

        for item in Data:

            if str(item.Userid) == str(decodedToken["user_id"]):

                ResponsedData[str(item)] = [item.id, item.Content, item.Status]       

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)    

        ResponsedData = {}

        Data = Task.objects.all()

        for item in Data:

            if str(item.Userid) == str(decodedToken["user_id"]):

                ResponsedData[str(item)] = [item.id, item.Content, item.Status]       

        Response = json.dumps(ResponsedData)

        return HttpResponse(Response)            

def NewAccount(request):

    NotMatchPass = {"Truthness":""}

    if request.method == 'POST':

        Name = request.POST.get('Name')

        Email = request.POST.get('Email')

        Password = request.POST.get('Password') 

        ConfirmPassword = request.POST.get('ConfirmPassword')

        if Password != ConfirmPassword :

            NotMatchPass = {"Truthness":"Incorrect Password Match"}

            return render(request, 'CreateAccount.html', NotMatchPass)

        else:

         AllUser = User.objects.all()

         if AllUser == None:

             NewUser = User(Name = Name, UserEmail = Email, Password = Password)

             NewUser.save()
            
             return redirect('/')

         else:

             try:

                SpecificUser = User.objects.get(UserEmail = Email, Password = Password)

                NotMatchPass = {"Truthness":"Matched Pair Error"}

                return render(request, 'CreateAccount.html', NotMatchPass)

             except:    

                NewUser = User(Name = Name, UserEmail = Email, Password = Password)

                NewUser.save()
            
                return redirect('/')  
    else:

        return render(request, 'CreateAccountJs.html', NotMatchPass)          

def LogIn(request):
    
    if request.method == 'POST':

            Email = request.POST.get('Email')

            Password = request.POST.get('Password') 

            try:

                SpecificUser = User.objects.get(UserEmail = Email, Password = Password)

                id = str(SpecificUser.id)

                SpecificUser.username = Email

                payload = jwt_payload_handler(SpecificUser)

                token = jwt_encode_handler(payload)

                ResponsedData = {"token" : token}

                Response = json.dumps(ResponsedData)

                return HttpResponse(Response)  

            except:

                return HttpResponse("Usename or Password is Wrong")

def JwtTokenDecode(CurrentUserToken):

    RealToken = CurrentUserToken.split(" ")

    IsExpire = round(time.time())

    DecodedToken = jwt_decode_handler(RealToken[1])

    TokenExpiryTime = DecodedToken["exp"]

    return DecodedToken