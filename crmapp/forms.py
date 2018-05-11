from django import forms
from crmapp.models import Partner


class PartnerCreateForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
