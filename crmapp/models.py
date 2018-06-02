import logging
from crmapp.management.commands import log_config
from crmapp.management.commands.loger import Log

from django.db import models

from decimal import *
from datetime import datetime

logger = logging.getLogger('update')
log = Log(logger)


class Bank(models.Model):
    name = models.CharField(verbose_name='назва банку', max_length=50)
    mfo = models.PositiveIntegerField(verbose_name='мфо', unique=True)

    def __str__(self):
        return self.name

    @log
    def upload_to_db(self, bank):
        row = bank
        new_bank = Bank(mfo=row[0], name=row[1])
        try:
            new_bank.save()
        except Exception as e:
            pass
        return new_bank.name


class Partner(models.Model):
    entity = models.BooleanField(verbose_name='юридична особа', default=False)
    full_name = models.CharField(verbose_name='повна назва підприємства', max_length=150)
    short_name = models.CharField(verbose_name='скорочена назва підприєства', max_length=80)
    inn = models.CharField(verbose_name='ідентификаційний номер', max_length=15, blank=True)
    edrpoy = models.CharField(verbose_name='єдрпоу', max_length=10, blank=True)
    dfro = models.CharField(verbose_name='дфро', max_length=15, blank=True)
    payment_account = models.CharField(verbose_name='розрахунковий рахунок', max_length=20, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, verbose_name='банк', default='')
    cert_vat = models.CharField(verbose_name='свідоцтво платника пдв', max_length=15, blank=True)
    dir_name = models.CharField(verbose_name='директор', max_length=150, blank=True)
    responsible = models.CharField(verbose_name='відповідальна особа', max_length=150, blank=True)
    phone1 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    phone2 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    phone3 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True)
    zipcode = models.PositiveIntegerField(verbose_name='поштовий індекс', default=0)
    country = models.CharField(verbose_name='країна', max_length=20, default='Україна')
    region = models.CharField(verbose_name='область', max_length=50, default='Волинська обл.')
    district = models.CharField(verbose_name='район', max_length=50, blank=True)
    town = models.CharField(verbose_name='населений пункт', max_length=50, blank=True)
    address = models.CharField(verbose_name='адреса', max_length=50, blank=True)

    def __str__(self):
        return self.short_name


class Firm(models.Model):
    full_name = models.CharField(verbose_name='повна назва підприємства', max_length=150)
    short_name = models.CharField(verbose_name='скорочена назва підприєства', max_length=80)
    inn = models.CharField(verbose_name='ідентификаційний номер', max_length=15, blank=True)
    edrpoy = models.CharField(verbose_name='єдрпоу', max_length=10, blank=True)
    dfro = models.CharField(verbose_name='дфро', max_length=15, blank=True)
    payment_account = models.CharField(verbose_name='розрахунковий рахунок', max_length=20, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, verbose_name='банк', default='')
    cert_vat = models.CharField(verbose_name='свідоцтво платника пдв', max_length=15, blank=True)
    dir_name = models.CharField(verbose_name='директор', max_length=150, blank=True)
    phone1 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    phone2 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    phone3 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True)
    zipcode = models.PositiveIntegerField(verbose_name='поштовий індекс', default=0)
    country = models.CharField(verbose_name='країна', max_length=20, default='Україна')
    region = models.CharField(verbose_name='область', max_length=50, default='Волинська обл.')
    district = models.CharField(verbose_name='район', max_length=50, blank=True)
    town = models.CharField(verbose_name='населений пункт', max_length=50, blank=True)
    address = models.CharField(verbose_name='адреса', max_length=50, blank=True)

    def __str__(self):
        return self.short_name


class Services(models.Model):
    name = models.CharField(verbose_name='послуга/робота', max_length=100, unique=True)


class Contract(models.Model):
    number = models.PositiveIntegerField(verbose_name='№ договору', unique=True)
    date_start = models.DateField(verbose_name='дата укладання')
    date_end = models.DateField(verbose_name='дата закінчення')
    client = models.ForeignKey(Partner, related_name='partner', verbose_name='замовник', on_delete=models.PROTECT)
    performer = models.ForeignKey(Firm, related_name='firm', verbose_name='виконавець', on_delete=models.PROTECT)
    works = models.TextField(verbose_name='предмет договору', help_text='заповніть через ;', blank=True)
    cost = models.DecimalField(verbose_name='вартість робіт', max_digits=10, decimal_places=2, blank=True,
                               default='0.00')
    vat = models.DecimalField(verbose_name='ПДВ', max_digits=10, decimal_places=2, blank=True, default='0.00')
    cost_vat = models.DecimalField(verbose_name='вартість з ПДВ', max_digits=10, decimal_places=2, blank=True,
                                   default='0.00')
    district = models.CharField(verbose_name='район', max_length=50, blank=True)
    town = models.CharField(verbose_name='населений пункт', max_length=50, blank=True)
    address = models.CharField(verbose_name='адреса', max_length=50, blank=True)
    note = models.TextField(verbose_name='примітка', blank=True)

    def __str__(self):
        return str(self.number)

    @staticmethod
    def get_contract(request):
        cost = request.get('cost')
        vat = Decimal(Decimal(cost) * Decimal(0.2)).quantize(Decimal('.00'))
        cost_vat = Decimal(Decimal(cost) * Decimal(1.2)).quantize(Decimal('.00'))
        client = Partner.objects.filter(pk=int(request.get('client'))).first()
        performer = Firm.objects.filter(pk=int(request.get('performer'))).first()
        contract = {
            'number': request.get('number'),
            'date_start': request.get('date_start'),
            'date_end': request.get('date_end'),
            'client': client,
            'performer': performer,
            'works': request.get('works'),
            'cost': cost,
            'vat': vat,
            'cost_vat': cost_vat,
            'district': request.get('district'),
            'town': request.get('town'),
            'address': request.get('address'),
            'note': request.get('note'),
        }
        return contract


class Invoice(models.Model):
    num_invoice = models.PositiveIntegerField(verbose_name='№ рахунку', blank=True)
    date_create = models.DateField(verbose_name='дата', default=datetime.strftime(datetime.today(), '%Y-%m-%d'))
    contract = models.ForeignKey(Contract, related_name='contract', verbose_name='договір', on_delete=models.PROTECT)
    performer = models.ForeignKey(Firm, related_name='performer', verbose_name='виконавець', on_delete=models.PROTECT)
    payer = models.ForeignKey(Partner, related_name='payer', verbose_name='платник', on_delete=models.PROTECT)
    works = models.TextField(verbose_name='назва', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='кількість', default=1)
    price = models.DecimalField(verbose_name='ціна', max_digits=10, decimal_places=2, blank=True,
                                default='0.00')
    vat = models.DecimalField(verbose_name='ПДВ', max_digits=10, decimal_places=2, blank=True, default='0.00')
    price_vat = models.DecimalField(verbose_name='ціна з ПДВ', max_digits=10, decimal_places=2, blank=True,
                                    default='0.00')
    is_paid = models.BooleanField(verbose_name='оплачений', default=False)

    def __str__(self):
        return str(self.num_invoice)

    @staticmethod
    def invoice_create(contract):
        invoice = Invoice(
            num_invoice=0,
            date_create=datetime.strftime(datetime.today(), '%d.%m.%Y'),
            contract=Contract.objects.filter(pk=int(contract.pk)).first(),
            performer=Firm.objects.filter(pk=int(contract.performer.pk)).first(),
            payer=Partner.objects.filter(pk=int(contract.client.pk)).first(),
            works=contract.works,
            price=contract.cost,
            vat=contract.vat,
            price_vat=contract.cost_vat
        )
        return invoice

    @staticmethod
    def get_invoice(request):
        price = request.get('price')
        vat = Decimal(Decimal(price) * Decimal(0.2)).quantize(Decimal('.00'))
        price_vat = Decimal(Decimal(price) * Decimal(1.2)).quantize(Decimal('.00'))
        contract = Contract.objects.filter(pk=int(request.get('contract'))).first()
        performer = Firm.objects.filter(pk=int(request.get('performer'))).first()
        payer = Partner.objects.filter(pk=int(request.get('payer'))).first()
        invoice = {
            'num_invoice': request.get('num_invoice'),
            'date_create': request.get('date_create'),
            'contract': contract,
            'performer': performer,
            'payer': payer,
            'works': request.get('works'),
            'quantity': request.get('quantity'),
            'price': price,
            'vat': vat,
            'price_vat': price_vat,
            'is_paid': request.get('is_paid'),
        }

        return invoice


class Act(models.Model):
    num_act = models.PositiveIntegerField(verbose_name='№ акту')
    date_create = models.DateField(verbose_name='дата', default=datetime.strftime(datetime.today(), '%Y-%m-%d'))
    contract = models.ForeignKey(Contract, related_name='act_contract', verbose_name='договір',
                                 on_delete=models.PROTECT)
    performer = models.ForeignKey(Firm, related_name='act_performer', verbose_name='виконавець',
                                  on_delete=models.PROTECT)
    client = models.ForeignKey(Partner, related_name='act_partner', verbose_name='замовник', on_delete=models.PROTECT)
    agent_firm = models.CharField(verbose_name='представник виконавця', max_length=150)
    agent_client = models.CharField(verbose_name='представник замовника', max_length=150)
    works = models.TextField(verbose_name='назва робіти, послуг', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='кількість', default=1)
    price = models.DecimalField(verbose_name='ціна', max_digits=10, decimal_places=2, blank=True,
                                default='0.00')
    vat = models.DecimalField(verbose_name='ПДВ', max_digits=10, decimal_places=2, blank=True, default='0.00')
    price_vat = models.DecimalField(verbose_name='ціна з ПДВ', max_digits=10, decimal_places=2, blank=True,
                                    default='0.00')

    def __str__(self):
        return str(self.num_act)

    @staticmethod
    def act_create(contract):
        act = Act(
            num_act=0,
            date_create=datetime.strftime(datetime.today(), '%d.%m.%Y'),
            contract=Contract.objects.filter(pk=int(contract.pk)).first(),
            performer=Firm.objects.filter(pk=int(contract.performer.pk)).first(),
            client=Partner.objects.filter(pk=int(contract.client.pk)).first(),
            works=contract.works,
            price=contract.cost,
            vat=contract.vat,
            price_vat=contract.cost_vat
        )
        return act
