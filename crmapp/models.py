import logging
from crmapp.management.commands import log_config
from crmapp.management.commands.loger import Log

from django.db import models

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
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
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
