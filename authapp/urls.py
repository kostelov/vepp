from django.urls import re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login, name='login'),
    # re_path(r'^login/$', authapp.LoginFormView.as_view(), name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
]
