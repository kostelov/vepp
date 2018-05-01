from django.urls import re_path
import crmapp.views as crmapp
import adminapp.views as adminapp

app_name = 'crmapp'

urlpatterns = [
    re_path(r'^$', crmapp.main_crm, name='main_crm'),
    re_path(r'^workers/list/$', crmapp.workers_list_view, name='workers_list'),
    re_path(r'^worker/detail/(?P<worker_pk>\d+)/$', crmapp.worker_detail_view, name='worker_detail'),
    re_path(r'^worker/update/(?P<worker_pk>\d+)/$', crmapp.worker_update_view, name='worker_update')
]
