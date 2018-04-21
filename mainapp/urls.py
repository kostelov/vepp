from django.urls import re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^voice/$', mainapp.voicep243, name='voicep243'),
    # re_path(r'^logout/$', authapp.logout, name='logout'),
]
