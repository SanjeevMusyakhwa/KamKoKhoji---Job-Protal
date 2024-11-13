from django import forms
from job.models import *

class CreateJobForm(forms.ModelForm):
  class Meta: 
    model = Job
    fields = ['user', 'post_date_time', 'date_posted', 'is_published']


class UpdateJobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['user', 'post_date_time', 'date_posted', 'is_published']

class AddJobResponsibilityForm(forms.ModelForm):
  class Meta:
    model = JobResponsibility
    fields = ['name']

class AddJobExperienceForm(forms.ModelForm):
  class Meta:
    model = JobExperiecnce
    fields = ['name']