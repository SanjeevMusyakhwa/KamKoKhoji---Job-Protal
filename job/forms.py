from django import forms
from job.models import *

class CreateJobForm(forms.ModelForm):
    class Meta: 
        model = Job
        exclude = ['post_date_time']  # Use only exclude or fields, not both

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['post_date_time']  # Use only exclude or fields, not both

class AddJobResponsibilityForm(forms.ModelForm):
    class Meta:
        model = JobResponsibility
        fields = ['name']

class AddJobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ['name']
