from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import GraphInput
from .forms import GraphInputForm, GraphOptionsForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

def main_page(request):
    return redirect('home:homepage')

def homepage(request):
    template = 'home/home.html'
    return render_to_response(template)

def graphplotter(request):

    if request.method == 'POST' and 'add' in request.POST:
        form = GraphInputForm(request.POST)
        print('Add Data')
        if form.is_valid():
            print('Form is valid')
            form.save()

    if request.method == 'GET':
        GraphInput.objects.all().delete()
        request.session['color_sel'] = 'red'
        request.session['plot_type'] = 'line'
        print('Clear Data')

    if request.method == 'POST' and 'colors' in request.POST:
        print('Color Selected')
        request.session['color_sel'] = request.POST['colors']

    if request.method == 'POST' and 'types' in request.POST:
        print('Line Selected')
        request.session['plot_type'] = request.POST['types']

    form = GraphInputForm()

    data = GraphInput.objects.all()
    template = 'home/plot.html'
    context = {'form': form, 'data': data}
    return render(request, template, context)


def page1(request):
    pass

def page2(request):
    if request.method == 'POST' and 'add' in request.POST:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST' and 'clear' in request.POST:
        GraphInput.objects.all().delete()
    form = GraphInputForm()

    data=GraphInput.objects.all()

    context = {'form': form, 'data':data}
    template = 'home/forms.html'
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

import django
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

def img(request):
    color_sel = request.session['color_sel']
    plot_type = request.session['plot_type']
    data_x=[]
    data_y=[]
    for key in GraphInput.objects.all():
        data_x.append(key.x)
        data_y.append(key.y)
    plt.Figure()
    x = data_x
    y = data_y
    if plot_type=='line':
        plt.plot(x, y, color=color_sel)
    elif plot_type=='scatter':
        plt.scatter(x, y, color=color_sel)
    else:
        plt.plot(x, y, color=color_sel)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close('all')
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response


def page_objects(request):
    if request.method == 'POST':
        print('Hiiiiii')
        form = GraphOptionsForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['col']
            return answer
    else: print('hello')
