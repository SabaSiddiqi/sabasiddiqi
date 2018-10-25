from django import forms
from .models import GraphInput, GraphOptions


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ('x', 'y')


class GraphOptionsForm(forms.ModelForm):
    class Meta:
        model = GraphOptions
        fields = ('color','type')
