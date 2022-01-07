from django.shortcuts import render
import joblib

def model(request):
    return render(request, 'fheart.html',{})

def modeloutput(request):
    file = joblib.load(open("heart.svc","rb"))
    cls = file

    lis = []
    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trtbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalachh'])
    lis.append(request.GET['exng'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slp'])
    lis.append(request.GET['caa'])
    lis.append(request.GET['thall'])
    
    output = cls.predict([lis])
    return render(request,"rheart.html",{"output":output})

# Create your views here.
