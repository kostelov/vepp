from django import forms
from crmapp.models import Partner, Firm, Services, Contract, Invoice


class PartnerCreateForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone1':
                field.help_text = 'приклад: +380998887766'


class FirmCreateForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone1':
                field.help_text = 'приклад: +380998887766'


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'vat' or field_name == 'cost_vat':
                field.widget.attrs['readonly'] = ''
            if field_name == 'works':
                field.help_text = 'вкажіть роботи розділяюючи їх ;'


class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'vat' or field_name == 'price_vat':
                field.widget.attrs['readonly'] = ''
