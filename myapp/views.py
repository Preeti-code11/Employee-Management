from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):

    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True
        
    

    date=datetime.datetime.now()
    
    name="codewithpreeti"
    listofprogams=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to check all prime numbers from 1 to 100',
        'WAP to print pascal'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"XYZ",
        'student_city':"AGRA"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':listofprogams,   
        'student_data':student
    }
    #return HttpResponse("<h1>Hello this is index page</h1>"+str(date))
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("This is about page")
    return render(request,"about.html",{})


def services(request):
    #return HttpResponse("This is services page")
    return render(request,"services.html",{})