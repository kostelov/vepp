import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from authapp.models import ProjectUser


class UserFormLogin(AuthenticationForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserFormLogin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


# форма редактирования профиля для администратора
class UserAdminUpdateForm(UserChangeForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name', 'last_name', 'parent_name', 'email', 'phone1', 'phone2', 'date_of_birth',
                  'avatar', 'is_active', 'is_dir', 'is_assistant', 'is_client', 'password')

    def __init__(self, *args, **kwargs):
        super(UserAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'avatar':
                # field.widget = forms.HiddenInput()
                field.widget.attrs['class'] = 'default'
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_phone1(self):
        # Проверям номер телефона согласно стандарта E.164
        tmpl = r'^\+{1}\d{10,14}\d$'
        data = self.cleaned_data['phone1']
        result = re.match(tmpl, data)
        if not result:
            raise forms.ValidationError('Укажите номер в международном формате')
        else:
            return data


# форма редактирования профиля для пользователя
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name', 'last_name', 'parent_name', 'email', 'phone1', 'phone2', 'date_of_birth',
                  'avatar', 'is_active', 'is_dir', 'is_assistant', 'is_client', 'password')

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'avatar':
                field.widget.attrs['class'] = 'default'
            if field_name == 'is_active' or field_name == 'is_dir' or \
                    field_name == 'is_assistant' or field_name == 'is_client' or field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_phone1(self):
        # Проверям номер телефона согласно стандарта E.164
        tmpl = r'^\+{1}\d{10,14}\d$'
        data = self.cleaned_data['phone1']
        result = re.match(tmpl, data)
        if not result:
            raise forms.ValidationError('Укажите номер в международном формате')
        else:
            return data


class UserPassChangeForm(AdminPasswordChangeForm):
    class Meta:
        model = ProjectUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserPassChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
