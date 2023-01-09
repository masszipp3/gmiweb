from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [ 

     path('',views.index,name='index'),
     path('addproduct',views.addproduct,name='addproduct'),

     path('login',views.adminlogin,name='adminlogin'),
     path('addreview',views.review,name='addreview'),
     path('viewproject',views.viewprojects,name='viewproject'),
     path('edit/<int:pid>',views.productedit,name='edit'),
     path('select/<int:pid>',views.select,name='select'),
     path('proim/<int:pid>',views.proimage,name='proimg'),
     path('img1/<int:pid>',views.img1,name='img1'),
     path('img2/<int:pid>',views.img2,name='img2'),
     path('img3/<int:pid>',views.img3,name='img3'),
     path('img4/<int:pid>',views.img4,name='img4'),
     path('delete/<int:pid>',views.delete,name='delete'),
     path('viewreviews',views.viewreviews,name='viewreviews'),
     path('deleterv/<int:pid>',views.deleterv,name='deleterv'),
     path('viewmsg',views.viewmsg,name='viewmsg'),
     path('addslides',views.addslides,name='addslides'),
     path('slides',views.viewslides,name='slides'),
     path('editslides/<int:pid>',views.editslides,name='editslides'),
     path('deleteslide/<int:pid>',views.deleteslide,name='deleteslider'),
     path('logout',views.logout,name='logout'),
 
]