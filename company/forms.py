from django import forms
from company.models import Company
from datetime import datetime

def possible_years(start, end):
    return [(str(year), str(year)) for year in range(start, end - 1, -1)]

class AddCompanyForm(forms.ModelForm):
    founded_in = forms.ChoiceField(choices=possible_years(datetime.now().year, 1900))
    
    class Meta:
        model = Company
        exclude = ['user']


class UpdateCompanyForm(forms.ModelForm):
  founded_in = forms.ChoiceField(choices=possible_years(datetime.now().year, 1900))

  class Meta:
    model = Company
    exclude = ['user']