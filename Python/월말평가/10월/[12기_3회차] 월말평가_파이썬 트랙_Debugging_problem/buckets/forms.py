from django import forms
from .models import TravelBucketList


class TravelBucketListForm(forms.ModelForm):
    class Meta:
        model = TravelBucketList
        # exclude 요소에 reason과 city를 추가해줌
        exclude = ('reason', 'city', )
        # 위젯에서 resaon과 city의 항목을 제거
        widgets = {
            'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'planned_visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
