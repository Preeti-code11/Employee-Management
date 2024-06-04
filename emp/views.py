from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp
from .models import Testimonial
from .forms import FeedbackForm, EmpForm

# Create your views here.
def emp_home(request):

    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #validate

        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.working=emp_working
        e.department=emp_department

        if e.working is None:
            e.working=False
        else:
            e.working=True

        #save the object
        e.save()

        #prepare msg
        print("data is coming")
        return redirect("/emp/home")
    form=EmpForm()
    form.save()
    return render(request,"emp/add_emp.html",{'form':form})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")
    
def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request, "emp/testimonials.html",{'testi':testi})

def feedback(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved")
    else:
        form=FeedbackForm()
        return render(request,"emp/feedback.html",{'form':form})