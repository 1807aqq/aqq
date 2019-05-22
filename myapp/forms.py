from django import forms
from myapp.models import User

class UserForm(forms.ModelForm):
    code = forms.CharField(required=True,
                           error_messages={
                               'required': '验证码不能为空'
                           })
    class Meta:
        model = User

