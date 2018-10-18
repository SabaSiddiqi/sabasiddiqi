from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Name

#Comments
    # Create your views here.
    # def view_name(request):
    #   return HttpResponse('text')
    #After adding template
    #   from django.shortcuts import render_to_response
    #   return render_to_response('app_name/template_name.html',{{'func_name':"text"}})
    #After adding model
    #   from .models import line
    #   return render_to_response('app_name/template_name.html',{'func_name_in_html':Line.objects.all() })

def main_page(request):
    return HttpResponse('You are on main page')

def homepage(request):
    #return HttpResponse('You are on home')
    #return render_to_response('home/home.html',{'hello':"Hey Hello"})
    return render_to_response('home/home.html',{'hello':Name.objects.all()})

def page1(request):
    return HttpResponse('You are on Page1')

def page2(request):
    return HttpResponse('You are on Page2')

def page3(request):
    return HttpResponse('You are on Page3')

def page4(request):
    return HttpResponse('You are on Page4')
