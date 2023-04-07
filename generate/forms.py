from django import forms

from generate.models import DataSchema


class CreateDataSchema(forms.ModelForm):
    name = forms.CharField()
    columns = forms.JSONField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = DataSchema
        fields = ['name', 'columns']
