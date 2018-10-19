from django import forms
from .models import GraphInput


class GraphForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ('x', 'y')
