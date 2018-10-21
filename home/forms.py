from django import forms
from .models import GraphInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class GraphForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login', css_class='btn-primary'))


class GraphInputForm(forms.ModelForm):
    x=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter x-coordinate'
            }
        )
    )
    y=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter y-coordinate'
            }
        )
    )
    class Meta:
        model = GraphInput
        fields = ('x', 'y')
