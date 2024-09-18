from django import forms
from . import models


class ExempleForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = '__all__'