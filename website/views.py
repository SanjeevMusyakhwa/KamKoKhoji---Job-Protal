from django.shortcuts import render
from job.models import Job
from company.models import Company

# Create your views here.
def HomePage(request):
  jobs = Job.objects.filter(status='Active').order_by('-post_date_time')[:4]
  companies = Company.objects.all()  # Renamed to avoid confusion with the loop variable
  return render(request, 'website/index.html', {'jobs': jobs, 'companies': companies})
