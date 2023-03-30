from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

import gmeuser


app_name = 'gmeuser'

handler404 = 'gmeuser.views.error_404'


urlpatterns = [ 

     path('',views.index,name='index'),
     path('projects',views.projects,name='projects'),
     path('contact',views.contact,name='contact'),
     path('reviews',views.review,name='review'),
     path('about',views.aboutus,name='about'),
     path('post/<int:pid>/<str:name>',views.post,name='post'),
     path('gmeedu',views.gmeedu,name='gmeedu'),
     path('error',views.maintainance,name='error'),
      path('/<str:name>',views.notfound,name='notfound'),
 
]