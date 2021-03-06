from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [

    #example - path( 'link/', views.view_name, name='view_name')
    #/home/
    path('',views.homepage, name='homepage'),
    #/home/1
    path('img.png/', views.img,name='img'),
    path('resume/', views.pdf_view,name='resume'),
    path('blog/', views.blogpage,name='blog'),
    path('recognize/', views.recognize,name='rec'),
    path('blog/<slug:blog_id>', views.blogdetail,name='blogdetail'),
    path('graphplotter_v1/', views.graphplotter,name='gplot'),
    path('graphplotter_v2/', views.graphplotterv2,name='gplot2'),
    path('table_download/', views.table_download,name='xlsx'),
]
