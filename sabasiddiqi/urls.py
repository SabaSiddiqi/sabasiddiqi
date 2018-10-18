from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [

    # example - path('link/',include('appname.urls'))
    # add include from django.urls
    # path('link/', views.link_view_name),

    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('home/', include('home.urls')),

]
