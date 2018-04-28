from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
# from django.views.generic.list import ListView

from authapp.models import ProjectUser
from authapp.forms import UserRegisterForm, UserAdminUpdateForm, UserPassChangeForm


# админка
@user_passes_test(lambda user: user.is_superuser)
def main_view(request):
    title = 'Адміністрування'
    count = ProjectUser.objects.all().count()

    context = {
        'title': title,
        'object': count,
    }
    return render(request, 'adminapp/index.html', context)


# просмотр списка зарегестрированных пользователей
@user_passes_test(lambda user: user.is_superuser)
def users_list_view(request):
    title = 'Користувачі'
    users_list = ProjectUser.objects.all().order_by('-is_active', 'username')

    context = {
        'title': title,
        'object_list': users_list,
    }
    return render(request, 'adminapp/users_list.html', context)


# создание пользователя
@user_passes_test(lambda user: user.is_superuser)
def user_create_view(request):
    title = 'Новий користувач'
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))
            except ValueError:
                pass

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'adminapp/user_create.html', context)


# просмотр детальной информации о пользователе
@user_passes_test(lambda user: user.is_superuser)
def user_detail_view(request, user_pk):
    title = 'Профіль користувача'
    user = get_object_or_404(ProjectUser, pk=user_pk)

    context = {
        'title': title,
        'object': user,
    }
    return render(request, 'adminapp/user_detail.html', context)


# редактирование профиля пользователя
# @user_passes_test(lambda user: user.is_superuser)
@login_required
def user_update_view(request, user_pk):
    title = 'Редагувати профіль'
    user = get_object_or_404(ProjectUser, pk=user_pk)
    if user:
        if request.method == 'POST':
            form = UserAdminUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))
        else:
            form = UserAdminUpdateForm(instance=user)

        context = {
            'title': title,
            'form': form,
            'object': user,
        }
        return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete_view(request, user_pk):
    user = get_object_or_404(ProjectUser, pk=int(user_pk))
    if user:
        user.is_active = False
        user.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_superuser)
def user_activate_view(request, user_pk):
    user = get_object_or_404(ProjectUser, pk=user_pk)
    if user:
        user.is_active = True
        user.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_superuser)
def user_change_password(request, user_pk):
    title = 'Зміна пароля користувача'
    user = get_object_or_404(ProjectUser, pk=user_pk)
    if user:
        if request.method == 'POST':
            form = UserPassChangeForm(user, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))
        else:
            form = UserPassChangeForm(user)

        context = {
            'title': title,
            'form': form,
            'object': user,
        }

        return render(request, 'adminapp/user_change_password.html', context)
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
