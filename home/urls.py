from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [

    #example - path( 'link/', views.view_name, name='view_name')
    #/home/
    path('',views.homepage, name='homepage'),
    #/home/1
    path('1/',views.page1, name='page1'),
    path('2/',views.page2, name='page2'),
    path('3/',views.page3, name='page3'),
    path('4/',views.page4, name='page4'),
    path('graph/',views.graph, name='graph'),
]
