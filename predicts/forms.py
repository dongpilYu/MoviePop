from django import forms
from .models import Predict


class PredictForm(forms.ModelForm):
    # 이 폼을 만들기 위해 어떤 model이 사용되어야 하는지 정의하는 코드
    class Meta:
        model = Predict
        fields = ['url', 'distributor']
        # 11-11
        # fields = ['naver_url', 'code', 'distributor']
