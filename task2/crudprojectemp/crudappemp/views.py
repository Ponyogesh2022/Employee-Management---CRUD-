from django.shortcuts import render,redirect
from .models import *
def index(request):
    return render(request,"add.html")
def addEmployee(request):
    if request.method=="POST":      
        eid=int(request.POST['eid'])
        ename=request.POST['ename']
        eemail=request.POST['eemail']
        ephno=request.POST['ephno']
        edob=request.POST['edob']
        lmd=request.POST['lmd']
        add=Employee(Employee_Id=eid,Employee_Name=ename,Employee_Email=eemail,Employee_PhoneNumber=ephno,Employee_DOB=edob,Last_Modified_Date=lmd)
        add.save()
        result="Information Saved"
        return render(request,"add.html",{'r':result})
    else:
        result="Information Not Saved"
        return render(request,"add.html",{'r':result})
def showall(request):
    show=Employee.objects.all()
    return render(request,'show.html',{'show':show})

def editEmployee(request,id):
    ap=Employee.objects.get(id=id)
    if request.method=="POST":      
        email=request.POST['eemail']
        phno=request.POST['ephno']
        dob=request.POST['edob']
        elmd=request.POST['lmd']
        ap.Employee_Email=email
        ap.Employee_PhoneNumber=phno
        ap.Employee_DOB=dob
        ap.Last_Modified_Date=elmd
        ap.save()
        return redirect('/show/')
    return render(request,'edit.html',{'i':ap})

def deleteEmployee(request,id):
    dele=Employee.objects.get(id=id)
    dele.delete()
    return redirect("/show/")

