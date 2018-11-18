from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import GraphInput
from .forms import GraphInputForm, GraphOptionsForm
from django.shortcuts import redirect
from django.http import FileResponse, Http404
import os
from sabasiddiqi.settings import MEDIA_ROOT
import io
import matplotlib.pyplot as plt

def main_page(request):
    return redirect('home:homepage')

def homepage(request):
    template = 'home/home.html'
    return render_to_response(template)

def graphplotterv2(request):

    if request.method == 'POST' and 'add' in request.POST:
        form = GraphInputForm(request.POST)
        if form.is_valid():
            form.save()

    #when the page refreshes
    if request.method == 'GET':
        GraphInput.objects.all().delete()
        request.session['color_sel'] = 'red'
        request.session['plot_type'] = 'line'
        request.session['title'] = 'Graph'
        request.session['xlabel'] = 'x-axis'
        request.session['ylabel'] = 'y-axis'

    if request.method == 'POST' and 'colors' in request.POST:
        print('Color Selected')
        request.session['color_sel'] = request.POST['colors']

    if request.method == 'POST' and 'labels' in request.POST:
        if request.POST['title']:   request.session['title'] = request.POST['title']
        if request.POST['xlabel']:  request.session['xlabel'] = request.POST['xlabel']
        if request.POST['ylabel']:  request.session['ylabel'] = request.POST['ylabel']

    if request.method == 'POST' and 'types' in request.POST:
        print('Line Selected')
        request.session['plot_type'] = request.POST['types']

    form = GraphInputForm()

    data = GraphInput.objects.all()
    template = 'home/plot2.html'
    context = {'form': form, 'data': data}
    return render(request, template, context)

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

def img(request):
    color_sel = request.session['color_sel']
    plot_type = request.session['plot_type']
    title_name = request.session['title']
    x_label = request.session['xlabel']
    y_label = request.session['ylabel']
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
    plt.title(title_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close('all')
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

def pdf_view(request):
    try:
        dir_name=MEDIA_ROOT
        base_filename='sabasiddiqi_resume'
        suffix = '.pdf'
        resume_path=os.path.join(dir_name, base_filename + suffix)
        return FileResponse(open(resume_path,'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    #C:\Users\sabas\Workspace\sabasiddiqi\sabasiddiqi\media\sabasiddiqi_resume.pdf
