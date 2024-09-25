from .models import Travel
from django import forms

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        label = 'Location',
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'ex) 제주도'
            }
        )
    )
    
    plan = forms.CharField(
        label = 'Location',
        widget= forms.Textarea(
            attrs = {
                'placeholder': 'ex) 슉, 슈슉.'
            }
        )
    )     
    start_date = forms.DateTimeField(
        label = 'Start date',
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'ex) 2022-02-02'
            }
        )
    )    
    end_date = forms.DateTimeField(
        label = 'End date',
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'ex) 2022-02-02'
            }
        )
    )    
    class Meta:
        model = Travel
        fields = '__all__'
