from .models import Resume, Education, Work
from django import forms

class CreateResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    exclude = ['user']

class UpdateResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    exclude = ['user']

class AddEducationForm(forms.ModelForm):
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