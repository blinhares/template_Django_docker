from django import forms
from . import models

class DateInput(forms.DateInput):
    """Cria um Widget para colocar datas."""

    input_type = 'date'
class ExempleForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = '__all__'
        widgets = {
            'pub_date': DateInput(),
        }