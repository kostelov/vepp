from datetime import datetime

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from authapp.models import ProjectUser
from authapp.forms import UserUpdateForm
from crmapp.forms import PartnerCreateForm, FirmCreateForm, ServiceCreateForm, ContractCreateForm, InvoiceCreateForm
from crmapp.models import Bank, Partner, Firm, Services, Contract, Invoice


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def main_crm(request):
    title = 'Панель керування'
    context = {
        'title': title,
    }
    return render(request, 'crmapp/index.html', context)


# просмотр списка сотрудников
@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
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
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def partners_view(request):
    title = 'Контрагенти'
    partners = Partner.objects.all()

    context = {
        'title': title,
        'object_list': partners
    }

    return render(request, 'crmapp/partners_list.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
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
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
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
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def partner_read_view(request, partner_pk):
    partner = get_object_or_404(Partner, pk=partner_pk)
    title = partner.short_name

    context = {
        'title': title,
        'object': partner,
    }

    return render(request, 'crmapp/partner_detail.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def firms_view(request):
    title = 'Фірми'
    firms = Firm.objects.all()

    context = {
        'title': title,
        'object_list': firms,
    }

    return render(request, 'crmapp/firms_list.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def firm_create_view(request):
    title = 'Додати фірму'
    banks = Bank.objects.all().order_by('name')
    if request.method == 'POST':
        form = FirmCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:firms'))
            except Exception as e:
                pass
    else:
        form = FirmCreateForm(initial={'banks': banks})

    context = {
        'title': title,
        'form': form,
        'banks': banks,
    }

    return render(request, 'crmapp/firm_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def firm_read_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    title = firm.short_name

    context = {
        'title': title,
        'object': firm,
    }

    return render(request, 'crmapp/firm_detail.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def firm_update_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    title = f'Редагувати фірму - {firm.short_name}'
    if request.method == 'POST':
        form = FirmCreateForm(request.POST, instance=firm)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:firm_read', kwargs={'firm_pk': firm.pk}))
            except Exception as e:
                pass
    else:
        form = FirmCreateForm(instance=firm)

    context = {
        'title': title,
        'form': form,
        'object': firm,
    }

    return render(request, 'crmapp/firm_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def services_view(request):
    title = 'Послуги'
    services = Services.objects.all()

    context = {
        'title': title,
        'object_list': services,
    }

    return render(request, 'crmapp/services_list.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def service_create_view(request):
    title = 'Додати роботу/послугу'
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:services'))
            except Exception as e:
                pass
    else:
        form = ServiceCreateForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'crmapp/service_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def service_update_view(request, service_pk):
    title = 'Редагувати послугу/роботу'
    service = get_object_or_404(Services, pk=service_pk)
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST, instance=service)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:services'))
            except Exception as e:
                pass
    else:
        form = ServiceCreateForm(instance=service)

    context = {
        'title': title,
        'form': form,
        'object': service,
    }

    return render(request, 'crmapp/service_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def contracts_view(request):
    title = 'Договора'
    contracts = Contract.objects.all().order_by('-date_start')

    context = {
        'title': title,
        'object_list': contracts,
    }

    return render(request, 'crmapp/contracts_list.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def contract_create_view(request):
    title = 'Додати договір'
    client = Partner.objects.all().order_by('short_name')
    performer = Firm.objects.all().order_by('short_name')
    if request.method == 'POST':
        form = ContractCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:contracts'))
            except Exception as e:
                pass
    else:
        form = ContractCreateForm(initial={'client': client, 'performer': performer})

    context = {
        'title': title,
        'form': form,
        'client': client,
        'performer': performer,
    }

    return render(request, 'crmapp/contract_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def contract_read_view(request, contract_pk):
    contract = get_object_or_404(Contract, pk=contract_pk)
    invoice = Invoice.objects.filter(contract__pk=contract_pk).exclude(num_invoice=0)
    dt = datetime.strftime(contract.date_start, '%d.%m.%Y')
    title = f'Договір № {contract.number} від {dt} р.'

    context = {
        'title': title,
        'object': contract,
        'invoice_list': invoice,
    }

    return render(request, 'crmapp/contract_detail.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def contract_update_view(request, contract_pk):
    title = 'Редагувати договір'
    contract = get_object_or_404(Contract, pk=contract_pk)
    if request.method == 'POST':
        form = ContractCreateForm(request.POST, instance=contract)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:contracts'))
            except Exception as e:
                pass
    else:
        form = ContractCreateForm(instance=contract)

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'crmapp/contract_update.html', context)


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def invoices_view(request):
    pass


@login_required
@user_passes_test(lambda user: user.is_assistant or user.is_superuser or user.is_dir)
def invoice_create_view(request, contract_pk):
    title = 'Новий рахунок'
    contract = get_object_or_404(Contract, pk=contract_pk)
    # создаем счет с нулевым номером и добалвяем в бд
    Invoice.objects.create(num_invoice=0, contract=contract, performer=contract.performer,
                                     payer=contract.client, works=contract.works, price=contract.cost)
    # выбираем созданный счет с нулевым номером и передаем в форму
    invoice = Invoice.objects.filter(num_invoice=0, contract=contract).first()
    if request.method == 'POST':
        form =  InvoiceCreateForm(request.POST, instance=invoice)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('crm:contracts'))
            except Exception as e:
                pass
    else:
        form = InvoiceCreateForm(instance=invoice)
        # данные в форме, удаляем "нулевой" счет
        invoice.delete()

    context = {
        'title': title,
        'contract': contract,
        'invoice': invoice,
        'form': form,
    }

    return render(request, 'crmapp/invoice_update.html', context)
