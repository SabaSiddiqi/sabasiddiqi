from django import forms
from .models import GraphInput


class GraphInputForm(forms.ModelForm):
    class Meta:
        model = GraphInput
        fields = ['x','y']
        widgets = {
            'x': forms.TextInput(attrs={'type': 'number','id':'form_homework','min': '-1000.00','max':'1000.00','step':'0.01'}),
            'y': forms.TextInput(attrs={'type': 'number','id':'form_homework','min': '-1000.00','max':'1000.00','step':'0.01'})
        }

from django import forms
from tinymce import TinyMCE
from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = '__all__'
