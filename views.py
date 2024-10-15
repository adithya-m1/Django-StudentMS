
from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
def demo(request):  
    return HttpResponse('Hello')

def greet(sd,n):
    return HttpResponse(f'<h1>Welcome django Workshop {n}</h1>')

def stdnt(req,a,b,c="VVIT"):
    return HttpResponse(f'<h1>College name: {c} <br> Student name: {a} <br>Student age: {b}</h1>')

def display(request):
    return HttpResponse("<h3> Welcome User <h3>")

def changecolor(req,name):
    return HttpResponse(f"<h2> Welcome user <span style='color:green;'>{name}</span></h2>")

def changestyle(req,ename,esal):
    return HttpResponse(f"<style> #ab{{color:blue;}} </style><h2> Employee Name:<span style='color:red'> {ename} </span> <br> Employee Salary: <span id='ab'>{esal}</span> </h2>")

def emp(req,ename,esal):
    return HttpResponse("<style> #ab{color:blue;} </style><h2> Employee Name:<span style='color:red'> "+ ename+" </span> <br> Employee Salary: <span id='ab'>"+str(esal)+"</span> </h2>")

def ry(req,name):
    return HttpResponse("<script>alert('WELCOME USER {0}');</script>".format(name))

def Student(req,name,age,rno,branch):
    return HttpResponse("<script>alert('Hi {0}');</script>"
                        "<html><table border=1><tr> <td>Name</td> <td>Age</td> <td>Rno</td> <td>branch<td> </tr> <tr> <td>{0}</td> <td>{1}</td> <td>{2}</td> <td>{3}</td> </tr> </table><html>".format(name,age,rno,branch)) 
def Student1(req,name,age,rno,branch):
    return HttpResponse("<script>alert('Hi {0}');</script>"
                        "<html><table border=1><tr> <td>Name</td> <td>{0}</td></tr> <tr> <td>branch</td> <td>{3}<td> </tr> <tr> <td>age</td> <td>{1}</td> </tr> <tr> <td>rno</td> <td>{2}</td> </tr> </table><html>".format(name,age,rno,branch))
def np(request):
    return render(request,'sample.html') 

def show(req):
    return HttpResponse("<html><style> div{display:flex;justify-content:center;height:100vh;}</style><div><h1>1.Albert Eeinstein <br> 2.Grahambell <br> 3.Nikola Tesla <br> 4.Thomas Alva Edison <br> 5.Alexander fleming</h1></div></html>")

def value(req,name):
    return render(req,'text1.html',{'z':name})

def employee(req,ename,esal,eage,eid):
    return render(req,'text1.html',{'a':ename,'b':esal,'c':eage,'d':eid})

def dr(req):
    if req.method=="POST":
        a=req.POST['rn']
        b=req.POST['sn']
        c=req.POST['sy']
        d=req.POST['sb']
        return render(req,'stdata.html',{'x':a,'y':b,'z':c,'w':d})
    return render(req,'student.html')


"""
introduction history pros and cons applications forms inline and blocked elements
difference between mvc and mvt
oops concepts
constructor and its types
inheritance and its concepts
bank application by using oops concepts
bootstrap4
(container-fluid,jumbotron,alerts,grid system)

dbms concepts(keys concepts)
bootstrap cards form controls

"""