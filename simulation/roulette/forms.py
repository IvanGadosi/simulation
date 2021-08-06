from django import forms
from .models import Graph


class GraphForm(forms.ModelForm):
    class Meta:
        model=Graph
        fields=(
            'turns',
            'money',
            'bet',
            'graph',
        )
        widgets = {'graph': forms.HiddenInput()}