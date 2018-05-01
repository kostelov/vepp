from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from authapp.models import ProjectUser
from authapp.forms import UserUpdateForm


@login_required
def main_crm(request):
    title = 'Панель керування'
    context = {
        'title': title,
    }
    return render(request, 'crmapp/index.html', context)


# просмотр списка сотрудников
@login_required
def workers_list_view(request):
    title = 'Працівники'
    users_list = ProjectUser.objects.all().order_by('-is_active', 'username')

    context = {
        'title': title,
        'object_list': users_list,
    }
    return render(request, 'crmapp/workers_list.html', context)


# просмотр детальной информации о пользователе
@login_required
def worker_detail_view(request, worker_pk):
    title = 'Профіль працівника'
    user = get_object_or_404(ProjectUser, pk=worker_pk)

    context = {
        'title': title,
        'object': user,
    }
    return render(request, 'crmapp/worker_detail.html', context)


@login_required
def worker_update_view(request, worker_pk):
    title = 'Редагувати профіль'
    user = get_object_or_404(ProjectUser, pk=worker_pk)
    if user:
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('crm:workers_list'))
        else:
            form = UserUpdateForm(instance=user)

        context = {
            'title': title,
            'form': form,
            'object': user,
        }
        return render(request, 'crmapp/worker_update.html', context)
