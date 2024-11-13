from django import forms
from company.models import Company

class AddCompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    exclude = ['user']

class UpdateComapnyForm(forms.ModelForm):
  class Meta:
    model = Company
    exclude = ['user']
