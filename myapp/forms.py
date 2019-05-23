from django import forms
from myapp.models import User

class UserForm(forms.ModelForm):
    code = forms.CharField(required=True,
                           error_messages={
                               'required': '验证码不能为空',
                               'min_length':'验证码必须是4位',
                               'max_length':"验证码必须是4位"
                           })
    class Meta:
        model = User
        fields = ['phone', 'phone-message', "passwd"]
