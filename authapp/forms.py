from django.contrib.auth.forms import AuthenticationForm
from django import forms
from authapp.models import ProjectUser


class UserFormLogin(AuthenticationForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserFormLogin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
