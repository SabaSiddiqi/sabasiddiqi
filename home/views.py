from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Name, GraphInput
from .forms import GraphForm, GraphInputForm


# Comments
# Create your views here.
# def view_name(request):
#   return HttpResponse('text')
# After adding template
#   from django.shortcuts import render_to_response
#   return render_to_response('app_name/template_name.html',{{'func_name':"text"}})
# After adding model
#   from .models import line
#   return render_to_response('app_name/template_name.html',{'func_name_in_html':Line.objects.all() })

def main_page(request):
    return HttpResponse('You are on main page')


def homepage(request):
    # return HttpResponse('You are on home')
    # return render_to_response('home/home.html',{'hello':"Hey Hello"})
    context = {'hello': Name.objects.all()}
    template = 'home/home.html'
    return render_to_response(template, context)


def page1(request):
    context = {'hello': Name.objects.all()}
    template = 'home/page1.html'
    return render_to_response(template, context)


def page2(request):
    if request.method == 'POST':
        form = GraphInputForm(request.POST)
        if form.is_valid():
            form.save()
    form = GraphInputForm()
    context = {'form': form}
    template = 'home/forms.html'
    # return render_to_response(template,context)
    return render(request, template, context)


def page3(request):
    return HttpResponse('You are on Page3')


def page4(request):
    return HttpResponse('You are on Page4')


def graph(request):
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            print(x, y)

    form = GraphForm()
    context = {'form': form}
    template = 'home/forms.html'
    # return render_to_response(template,context)
    return render(request, template, context)
