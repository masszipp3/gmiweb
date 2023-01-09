from django.shortcuts import render
from gmeuser.models import ProjectDetails
from gmeuser.models import ReviewDetails
from gmeuser.models import Msgs
from adminapp.models import Slides

# Create your views here.

def index(request):
    try:
        project = ProjectDetails.objects.all()
        slide = Slides.objects.all()
        projectObj = []
        for i in range(0, 6):
            projectObj.append(project[i])

        print(projectObj)
        return render(request,'gmehome/index.html',{'details': projectObj,'slid':slide})
    except:
        try:
         return render(request,'gmehome/index.html',{'details': project,'slid':slide})
        except:
             return render(request,'gmehome/maintaiance.html',{'details': project,'slid':slide})




def projects(request):
    try:

        project = ProjectDetails.objects.all()
        return render(request,'gmehome/projects.html',{'details': project})   
    except:
        try:
            return render(request,'gmehome/projects.html')
        except:
            return render(request,'gmehome/maintainance.html')    

def contact(request):
    msg=''
    try:
        if request.method == 'POST':
            cname = request.POST['cname']
            mobile = request.POST['mobile']
            email = request.POST['email']
            message = request.POST['message']
            rvs = Msgs(Name=cname,Email=email,Phone=mobile,Message=message)
            rvs.save()
            msg='Message have sent successfully'
        return render(request,'gmehome/contactus.html',{'status':msg})
    except:
         msg='Unable to send'
         return render(request,'gmehome/contactus.html',{'status':msg})    

def review(request):

    try:
        review=ReviewDetails.objects.all()
        return render(request,'gmehome/reviews.html',{'rvdetails':review})   
    except:
        try:
         return render(request,'gmehome/reviews.html')
        except:
            return render(request,'gmehome/maintainance.html')



def aboutus(request):
    return render(request,'gmehome/aboutus.html')         

def post(request,pid,name):
    try:
        prodeta=ProjectDetails.objects.get(id=pid,title=name)
        return render(request,'gmehome/post.html',{'key':prodeta})   

    except:
         return render(request,'ghome/index.html') 

def gmeedu(request):
    return render(request,'gmehome/gmedu.html')     

def maintainance(request):
    return render(request,'gmehome/maintainance.html')         
