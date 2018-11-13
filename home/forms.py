from django import forms
from .models import GraphInput, GraphOptions


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ['x','y']
        widgets = {
            'x': forms.TextInput(attrs={'size':'10','maxlength':'3'}),
            'y': forms.TextInput(attrs={'size':'10', 'maxlength':'3'})
        }


class GraphOptionsForm(forms.ModelForm):
    class Meta:
        model = GraphOptions
        fields = ['color','type']
