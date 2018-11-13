from django import forms
from .models import GraphInput, GraphOptions


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ['x','y']
        widgets = {
            'x': forms.TextInput(attrs={'type': 'number','id':'form_homework','min': '-1000.00','max':'1000.00','step':'0.01'}),
            'y': forms.TextInput(attrs={'type': 'number','id':'form_homework','min': '-1000.00','max':'1000.00','step':'0.01'})
        }


class GraphOptionsForm(forms.ModelForm):
    class Meta:
        model = GraphOptions
        fields = ['color','type']
