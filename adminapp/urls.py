from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main_view, name='admin'),
    re_path(r'^users/list/$', adminapp.users_list_view, name='users'),
    re_path(r'^user/create/$', adminapp.user_create_view, name='user_create'),
    re_path(r'^user/read/(?P<user_pk>\d+)/$', adminapp.user_detail_view, name='user_detail'),
    re_path(r'^user/update/(?P<user_pk>\d+)/$', adminapp.user_update_view, name='user_update'),
    # re_path(r'^user/delete/$', adminapp.user_delete_view, name='user_delete'),
    # re_path(r'^users/read/$', adminapp.UserListView.as_view(), name='users'),
]
