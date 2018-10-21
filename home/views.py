from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Name, GraphInput
from .forms import GraphForm, GraphInputForm


class page2form(TemplateView):

    template_name = 'home/forms.html'

    def get(self, request):
        form=GraphInputForm()
        data=GraphInput.objects.all()
        context = {'form': form,'data':data}
        return render(request, self.template_name, context)

    def page2(self, request):
        if request.method == 'POST':
            form = GraphInputForm(request.POST)
            if form.is_valid():
                form.save()
        form = GraphInputForm()
        context = {'form': form}
        # return render_to_response(template,context)
        return render(request, self.template_name, context)

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
