import django_filters

from job.models import Job

class JobFilter(django_filters.FilterSet):
  class Meta:
    model = Job
    fields = ['title']