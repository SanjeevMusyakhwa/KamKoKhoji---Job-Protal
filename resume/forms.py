from .models import Resume, Education, Work
from django import forms
from datetime import datetime

def possible_years(start, end):
    return [(str(year), str(year)) for year in range(start, end - 1, -1)]

class CreateResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    exclude = ['user']

class UpdateResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    exclude = ['user']

class AddEducationForm(forms.ModelForm):
  start_year = forms.ChoiceField(choices=possible_years(datetime.now().year, 1900))
  end_year = forms.ChoiceField(choices=possible_years(datetime.now().year, 1900))

  class Meta:
    model = Education
    exclude = ['resume']

class UpdateEducationForm(forms.ModelForm):
  class Meta:
    model = Education
    exclude = ['resume']

class AddWorkForm(forms.ModelForm):
  class Meta:
    model = Work
    exclude = ['resume']

class UpdateWorkForm(forms.ModelForm):
  class Meta:
    model = Work
    exclude = ['resume']