from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # example - path('link/',include('appname.urls'))
    # add include from django.urls
    # path('link/', views.link_view_name),

    path('admin/', admin.site.urls),
    path('', views.main_page , name='mainpage'),
    path('home/', include('home.urls',namespace='home')),

]


#https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
