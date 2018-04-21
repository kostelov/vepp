from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView

from authapp.models import ProjectUser


@user_passes_test(lambda user: user.is_superuser)
def main_view(request):
    title = 'Адміністрування'
    count = ProjectUser.objects.all().count()

    context = {
        'title': title,
        'object': count,
    }
    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda user: user.is_superuser)
def users_list_view(request):
    title = 'Користувачі'
    users_list = ProjectUser.objects.all().order_by('-is_active', 'username')

    context = {
        'title': title,
        'object_list': users_list,
    }
    return render(request, 'adminapp/users_list.html', context)

# class UserListView(ListView):
#     model = ProjectUser
#     template_name = 'adminapp/users_list.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Користувачі'
#         return context
#
#     @method_decorator(user_passes_test(lambda user: user.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
