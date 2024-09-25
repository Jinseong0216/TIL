from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label = 'Summary',
        widget= forms.TextInput(
            attrs = {
                "placeholder": "summary",
            }
        )
    )
    memo = forms.CharField(
        label = 'Memo', 
        widget= forms.Textarea(
            attrs = {
                "placeholder": "memo",
                "rows": 5,
                "cols": 50,
            }
        )
    )    
    class Meta:
        model = Memo
        fields = '__all__'