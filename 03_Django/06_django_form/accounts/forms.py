from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model() #user 라는 모델은 디렉트하게 작용하면 안됀당,, 공식룰
        fields = ('email', 'first_name', 'last_name',)