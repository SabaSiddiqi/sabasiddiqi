from django.shortcuts import render, render_to_response
from .models import GraphInput
from .forms import GraphInputForm
from django.shortcuts import redirect
from django.http import FileResponse, Http404, HttpResponse
import os
from sabasiddiqi.settings import MEDIA_ROOT
import io
import matplotlib.pyplot as plt
import xlsxwriter

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

#https://stackoverflow.com/questions/39394861/read-django-data-from-model-and-write-it-using-xlsxwriter
def table_download(request):
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('Reporte3a5')
    bold = workbook.add_format({'bold': True})
    # Some data we want to write to the worksheet.
    reporte = GraphInput.objects.all() #my model

    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for linea in reporte:
        worksheet.write(row, col, linea.x)
        worksheet.write(row, col + 1, linea.y)
        #worksheet.write(row, col + 2, linea.ship_set)
        row += 1

    # Write the title for every column in bold
    worksheet.write('A1','X-Coordinate', bold)
    worksheet.write('B1', 'Y-Coordinate', bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Reporte3a5.xlsx"

    return response
