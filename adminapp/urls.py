from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main_view, name='main'),
    re_path(r'^users/read/$', adminapp.users_list_view, name='users'),
    # re_path(r'^users/read/$', adminapp.UserListView.as_view(), name='users'),
    # re_path(r'^login/$', authapp.LoginFormView.as_view(), name='login'),
    # re_path(r'^logout/$', authapp.logout, name='logout'),
]
