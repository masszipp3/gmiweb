from django.shortcuts import render,redirect
from gmeuser.models import ProjectDetails
from gmeuser.models import ReviewDetails
from gmeuser.models import Msgs
from .models import Slides
from .models import Login
from .decorators import auth_admin

# Create your views here.

@auth_admin
def index(request):
    admin=Login.objects.get(id=request.session['adminid'])
    return render(request,'adminhome/index.html')

def adminlogin(request):
    if request.method == 'POST':
        auser = request.POST['username']
        puser = request.POST['password']
        try:
            alogin = Login.objects.get(username=auser,password=puser)
            request.session['adminid']=alogin.id
            return redirect("adminapp:index")
        except:
            msg='Username or Password incorrect'
            return render(request,'adminhome/adminlogin.html',{'status':msg}) 


    
    return render(request,'adminhome/adminlogin.html')    

@auth_admin
def addproduct(request):
    msg=''

    try:

        if request.method == 'POST':
            ptitle = request. POST['s_desc']
            complete_desc = request.POST['full_desc']
            upload_pic = request.FILES['pro_pic']
            try :
                iimage_1 = request.FILES['img_1'] 
            except:
                iimage_1 = ''
            try:
                iimage_2 = request.FILES['img_2'] 
            except:
                 iimage_2 = ''
            try:

              iimage_3 = request.FILES['img_3'] 
            except:
                iimage_3=''  
            try:

             iimage_4 = request.FILES['img_4'] 
            except:
                iimage_4=''
            pcatagory = request.POST['category']
            proj = ProjectDetails(title = ptitle,description = complete_desc,project_image = upload_pic,image_1 = iimage_1,image_2 = iimage_2 ,image_3 =  iimage_3 ,image_4 = iimage_4, catagory=pcatagory)
            proj.save()
            msg='Product added Succesfully'
        return render(request,'adminhome/addproduct.html',{'status':msg}) 

    except:
        msg='Some Error Occured'
        return render(request,'adminhome/addproduct.html',{'status':msg}) 

@auth_admin
def review(request):
    msg=''
    try:
        if request.method == 'POST':
            cname = request.POST['cname']
            mobile = request.POST['mobile']
            email = request.POST['email']
            place = request.POST['place']
            rating = request.POST['rating']
            reviews = request.POST['review'] 
            rvs = ReviewDetails(Customername=cname,Emailid=email,Rating=rating,Mobile=mobile,Place=place,Review=reviews)
            rvs.save()
            msg='Reiew added succesfully'


        return render(request,'adminhome/addreview.html',{'status':msg})
    except:
        msg='error occured'
        return render(request,'adminhome/addreview.html',{'status':msg})

@auth_admin
def viewprojects(request):

    view = ProjectDetails.objects.all()

    return render(request,'adminhome/viewproject.html',{'list': view})      

@auth_admin
def productedit(request,pid):
    msg=''
    try:
    
        if request.method == 'POST':
            proj = ProjectDetails.objects.get(id=pid)
            proj.title = request. POST['s_desc']
            proj.description = request.POST['full_desc']
            proj.catagory = request.POST['category']    
            proj.save()
            msg='Product Edited Succesfully'

        edits = ProjectDetails.objects.get(id=pid)
        
        return render(request,'adminhome/projectedit.html',{'edit': edits,'status':msg})  
    except:
        msg='some error occured'
        edits = ProjectDetails.objects.get(id=pid)
        return render(request,'adminhome/projectedit.html',{'edit': edits,'status':msg})


@auth_admin
def select(request,pid):

    imgs = ProjectDetails.objects.get(id=pid)

    return render(request,'adminhome/selectimage.html',{'imgs': imgs})        

@auth_admin
def proimage(request,pid):
    msg=''
    proim = ProjectDetails.objects.get(id=pid)
    try:
        if request.method=='POST':
            proim = ProjectDetails.objects.get(id=pid)
            img = request.FILES['pro_pic']
            proim.project_image=img
            proim.save()
            msg='file changed successfully'

        return render(request,'adminhome/proimage.html',{'pro': proim,'msg':msg})    

    except:
        msg='no file selected'
        return render(request,'adminhome/proimage.html',{'pro': proim,'msg':msg})


@auth_admin
def img1(request,pid):
    msg=''
    proim = ProjectDetails.objects.get(id=pid)
    try:
        if request.method=='POST':
            proim = ProjectDetails.objects.get(id=pid)
            img = request.FILES['img_1']
            proim.image_1=img
            proim.save()
            msg='file changed successfully'

        return render(request,'adminhome/img1.html',{'img1': proim,'msg':msg})   
    except:
        msg='no file selected'
        return render(request,'adminhome/img1.html',{'img1': proim,'msg':msg})  

@auth_admin
def img2(request,pid):
    msg=''
    proim = ProjectDetails.objects.get(id=pid)
    try:
        if request.method=='POST':
            proim = ProjectDetails.objects.get(id=pid)
            img = request.FILES['img2']
            proim.image_2=img
            proim.save()
            msg='file changed successfully'

        return render(request,'adminhome/img2.html',{'img2': proim,'msg':msg}) 
    except:
        msg='no file selected'
        return render(request,'adminhome/img2.html',{'img2': proim,'msg':msg}) 

@auth_admin
def img3(request,pid):
    msg=''
    proim = ProjectDetails.objects.get(id=pid)
    try:
        if request.method=='POST':
            proim = ProjectDetails.objects.get(id=pid)
            img = request.FILES['img_3']
            proim.image_3=img
            proim.save()
            msg='file changed successfully'
        return render(request,'adminhome/img3.html',{'img3': proim,'msg':msg}) 
    except:
        msg='no file selected'
        return render(request,'adminhome/img3.html',{'img3': proim,'msg':msg}) 

@auth_admin
def img4(request,pid):
    msg=''
    proim = ProjectDetails.objects.get(id=pid)
    try:
        if request.method=='POST':
            proim = ProjectDetails.objects.get(id=pid)
            img = request.FILES['img_4']
            proim.image_4=img
            proim.save()
            msg='file changed successfully'
        return render(request,'adminhome/img4.html',{'img4': proim,'msg':msg})    
    except:
        msg='no file selected'
        return render(request,'adminhome/img4.html',{'img4': proim,'msg':msg})

@auth_admin
def delete(request,pid):   
  pdelete=  ProjectDetails.objects.filter(id=pid) 
  view= ProjectDetails.objects.all()
  pdelete.delete()
  msg='project deleted successfully'
  return render(request,'adminhome/viewproject.html',{'list': view,'msg':msg})

@auth_admin
def viewreviews(request):
    view = ReviewDetails.objects.all()
    return render(request,'adminhome/viewreviews.html',{'list': view})  
@auth_admin
def deleterv(request,pid):   
  pdelete=  ReviewDetails.objects.filter(id=pid) 
  view= ReviewDetails.objects.all()
  pdelete.delete()
  msg='review deleted successfully'
  return render(request,'adminhome/viewreviews.html',{'list': view,'msg':msg})    

@auth_admin
def viewmsg(request):
    view = Msgs.objects.all()

    return render(request,'adminhome/viewmsgs.html',{'list': view}) 

@auth_admin
def viewslides(request):
    view = Slides.objects.all()

    return render(request,'adminhome/slides.html',{'list': view})       

@auth_admin
def addslides(request):
    msg=''

    try:

        if request.method == 'POST':
            slide_1 = request.FILES['img_1']
            proj = Slides(image_1 = slide_1)
            proj.save()
            msg='Slide Image Added Succesfully'
        return render(request,'adminhome/addslides.html',{'status':msg}) 

    except:
        msg='Some Error Occured'
        return render(request,'adminhome/addslides.html',{'status':msg}) 

def deleteslide(request,pid):   
  try:
    pdelete=  Slides.objects.filter(id=pid) 
    view= Slides.objects.all()
    pdelete.delete()
    msg='slide deleted successfully'
    return render(request,'adminhome/slides.html',{'list': view,'msg':msg})    

  except:
     msg='error occured '
     view= Slides.objects.all()
     return render(request,'adminhome/slides.html',{'list': view,'msg':msg})  

@auth_admin
def editslides(request,pid):
    msg=''
    proj = Slides.objects.get(id=pid)
    try:
        if request.method == 'POST':
            proj.image_1 = request.FILES['img_1'] 
            proj.save()
            msg='Slide Edited Succesfully'
        return render(request,'adminhome/editslides.html',{'edit':proj,'status':msg})  
    except:
        msg='some error occured'
        edits = Slides.objects.get(id=pid)
        return render(request,'adminhome/editslides.html',{'edit':edits,'status':msg})
        
def logout(request):
    del request.session['adminid']
    request.session.flush()
    return redirect('adminapp:adminlogin')         


                                 

   