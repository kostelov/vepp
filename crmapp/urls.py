from django.urls import re_path
import crmapp.views as crmapp

app_name = 'crmapp'

urlpatterns = [
    # работники
    re_path(r'^$', crmapp.main_crm, name='main_crm'),
    re_path(r'^workers/list/$', crmapp.workers_list_view, name='workers_list'),
    re_path(r'^worker/detail/(?P<worker_pk>\d+)/$', crmapp.worker_detail_view, name='worker_detail'),
    re_path(r'^worker/update/(?P<worker_pk>\d+)/$', crmapp.worker_update_view, name='worker_update'),
    # контрагенты
    re_path(r'^partners/$', crmapp.partners_view, name='partners'),
    re_path(r'^partner/create/$', crmapp.partner_create_view, name='partner_create'),
    re_path(r'^partner/read/(?P<partner_pk>\d+)/$', crmapp.partner_read_view, name='partner_read'),
    re_path(r'^partner/update/(?P<partner_pk>\d+)/$', crmapp.partner_update_view, name='partner_update'),
    # фирмы
    re_path(r'^firms/$', crmapp.firms_view, name='firms'),
    re_path(r'^firm/create/$', crmapp.firm_create_view, name='firm_create'),
    re_path(r'^firm/read/(?P<firm_pk>\d+)/$', crmapp.firm_read_view, name='firm_read'),
    re_path(r'^firm/update/(?P<firm_pk>\d+)/$', crmapp.firm_update_view, name='firm_update'),
    # работы/услуги
    re_path(r'^services/$', crmapp.services_view, name='services'),
    re_path(r'^service/create/$', crmapp.service_create_view, name='service_create'),
    re_path(r'^service/update/(?P<service_pk>\d+)/$', crmapp.service_update_view, name='service_update'),
    # договора
    re_path(r'^contracts/$', crmapp.contracts_view, name='contracts'),
    re_path(r'^contract/create/$', crmapp.contract_create_view, name='contract_create'),
    re_path(r'^contract/read/(?P<contract_pk>\d+)/$', crmapp.contract_read_view, name='contract_read'),
    re_path(r'^contract/update/(?P<contract_pk>\d+)/$', crmapp.contract_update_view, name='contract_update'),
    re_path(r'^contract/edit/$', crmapp.contract_edit_view),
    # счета
    re_path(r'^invoices/$', crmapp.invoices_view, name='invoices'),
    re_path(r'^invoice/create/(?P<contract_pk>\d+)$', crmapp.invoice_create_view, name='invoice_create'),
    re_path(r'^invoice/read/(?P<invoice_pk>\d+)$', crmapp.invoice_read_view, name='invoice_read'),
    re_path(r'^invoice/update/(?P<invoice_pk>\d+)$', crmapp.invoice_update_view, name='invoice_update'),
    re_path(r'^invoice/edit/$', crmapp.invoice_edit_view),
    # акты
    re_path(r'^acts/$', crmapp.acts_view, name='acts'),
    re_path(r'^act/create/(?P<contract_pk>\d+)/$', crmapp.act_create_view, name='act_create'),
    re_path(r'^act/read/(?P<act_pk>\d+)/$', crmapp.act_read_view, name='act_read'),
    re_path(r'^act/update/(?P<act_pk>\d+)/$', crmapp.act_update_view, name='act_update'),
    # проекты
    re_path(r'^projects/$', crmapp.projects_view, name='projects'),
    re_path(r'^project/create/(?P<contract_pk>\d+)$', crmapp.project_create_view, name='project_create'),
    # re_path(r'^project/read/(?P<project_pk>\d+)$', crmapp.project_read_view, name='project_read'),
    re_path(r'^project/update/(?P<project_pk>\d+)$', crmapp.project_update_view, name='project_update'),
    # задачи
    # re_path(r'^tasks/$', crmapp.tasks_view, name='tasks'),
    re_path(r'^task/create/(?P<project_pk>\d+)$', crmapp.task_create_view, name='task_create'),
    # re_path(r'^task/read/(?P<project_pk>\d+)$', crmapp.project_read_view, name='project_read'),
    re_path(r'^task/update/(?P<task_pk>\d+)$', crmapp.task_update_view, name='task_update'),
]
