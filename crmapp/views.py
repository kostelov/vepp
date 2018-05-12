from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from authapp.models import ProjectUser
from authapp.forms import UserUpdateForm
from crmapp.forms import PartnerCreateForm
from crmapp.models import Bank, Partner


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


@login_required
def partners_view(request):
    title = 'Контрагенти'
    partners = Partner.objects.all()

    context = {
        'title': title,
        'object_list': partners
    }

    return render(request, 'crmapp/partners_list.html', context)


@login_required
def partner_create_view(request):
    title = 'Додати контрагента'
    banks = Bank.objects.all().order_by('name')
    if request.method == 'POST':
        form = PartnerCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:partners'))
            except Exception as e:
                pass
    else:
        form = PartnerCreateForm(initial={'banks': banks})

    context = {
        'title': title,
        'banks': banks,
        'form': form,
    }

    return render(request, 'crmapp/partner_update.html', context)


@login_required
def partner_update_view(request, partner_pk):
    partner = get_object_or_404(Partner, pk=partner_pk)
    title = f'Редагувати контрагента - {partner.short_name}'
    if request.method == 'POST':
        form = PartnerCreateForm(request.POST, instance=partner)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:partner_read', kwargs={'partner_pk': partner.pk}))
            except Exception as e:
                pass
    else:
        form = PartnerCreateForm(instance=partner)

    context = {
        'title': title,
        'form': form,
        'object': partner,
    }

    return render(request, 'crmapp/partner_update.html', context)


@login_required
def partner_read_view(request, partner_pk):
    partner = get_object_or_404(Partner, pk=partner_pk)
    title = partner.short_name

    context = {
        'title': title,
        'object': partner
    }

    return render(request, 'crmapp/partner_detail.html', context)


@login_required
def firms_view(request):
    title = 'Фірми'
    # partners = Partner.objects.all()

    context = {
        'title': title,
        # 'object_list': partners
    }

    return render(request, 'crmapp/firms_list.html', context)