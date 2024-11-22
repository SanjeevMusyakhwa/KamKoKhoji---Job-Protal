from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model

def createjob(request):
  if request.method == 'POST':
    form = CreateJobForm(request.POST)
    if form.is_valid():
      job = form.save(commit=False)
      company = Company.objects.get(pk = request.user.company.pk)
      job.company = company
      job.save()
      messages.success(request,"Job has Been Created.")
      print('Job Created')
      return redirect('job:joblist_percompany')
    else:
      messages.warning(request,'Something went wrong, Please try again later')
      print('Job Not  Created')
      return redirect('job:create_job')
  else:
    form = CreateJobForm()
    context = {'form': form}
  return render(request, 'job/create_job.html', context)

def update_job(request, pk):
  job = Job.objects.get(id = pk)
  if request.method == 'POST':
    form = UpdateJobForm(request.POST, instance=job)
    if form.is_valid():
      form.save()
      messages.success(request, "Job Information updated Successfully..")
      return redirect(reverse('job:job_details', args=[job.pk]))
    else:
      messages.warning(request, 'Something went wrong')
      return redirect(reverse('company:company_details', args=[job.pk]))
  else:
    form = UpdateJobForm(instance = job)
    context = {'form':form}
  return render(request, 'job/update_job.html', context)

def delete_job(request,pk):
  job = Job.objects.get(id = pk)
  job.delete()
  messages.success(request, "Job Deleted Successfully")
  return redirect('job:joblist_percompany')

def joblist_percompany(request):
  company = Company.objects.get(pk = request.user.company.pk)
  jobs = company.job_set.all().order_by('-id')
  context = {'jobs': jobs}
  return render(request, 'job/joblist_percompany.html', context)

def job_details(request, pk):
  job = Job.objects.get(id = pk)
  company = Company.objects.get(pk=job.company.pk)
  context = {'job': job, 'company':company}
  return render(request, 'job/job_details.html', context)

def add_jobresponsibility(request, pk):
  job = Job.objects.get(pk = pk)
  if request.method == 'POST':
    form = AddJobResponsibilityForm(request.POST)
    if form.is_valid():
      jobres = form.save(commit=False)
      jobres.job = job
      jobres.save()
      messages.success(request, "Job Responsibility added successfully")
      return redirect(reverse('job:job_details', args= [job.pk]))
    else:
      messages.warning(request,"Something went wrong")
      return redirect(reverse('job:add_jobresponsibility', args= [job.pk]))
  else:
    form = AddJobResponsibilityForm()
    context = {'form': form, 'job':job}
  return render(request, 'job/add_jobresponsibility.html', context)

def add_jobexperience(request, pk):
  job = Job.objects.get(id = pk)
  if request.method == 'POST':
    form = AddJobExperienceForm(request.POST)
    if form.is_valid():
      jobexp = form.save(commit=False)
      jobexp.job = job
      jobexp.save()
      messages.success(request,"Job Experience added")
      return redirect(reverse('job:job_details', args = [job.pk]))
    else:
      messages.warning(request, 'something went worng')
      return redirect(reverse('job:add_jobexperience', args = [job.pk]))
  else:
    form = AddJobExperienceForm()
    context = {'form': form, 'job':job}
  return render(request, 'job/add_jobexperience.html', context)

def delete_jobresponsibility(request, pk):
  jobres = JobResponsibility.objects.get(id = pk)
  get_job = jobres.job 
  jobres.delete()
  messages.success(request,'Job Responsibility deleted successfully')
  return redirect(reverse('job:job_details', args=[get_job.pk]))


def delete_jobexperience(request, pk):
  jobexp = JobExperience.objects.get(id = pk)
  get_job = jobexp.job 
  jobexp.delete()
  messages.success(request,'Job Experience deleted successfully')
  return redirect(reverse('job:job_details', args=[get_job.pk]))


def all_joblist(request):
  jobs = Job.objects.filter(status = 'Active')
  context = {'jobs': jobs}
  return render(request, 'job/all_joblist.html', context)

def apply_for_job(request, pk):
    # Fetch the job or return 404 if not found
    job = get_object_or_404(Job, id=pk)

    # Check if the job is active
    if job.status != 'Active':
        messages.warning(request, 'This job is no longer available.')
        return redirect(reverse('job:all_joblist'))

    # Check if the user has a resume
    if not getattr(request.user, 'resume', None):
        messages.warning(request, 'You don\'t have a resume. Please create one before applying for jobs.')
        return redirect(reverse('job:all_joblist'))

    # Check if the user has already applied for this job
    has_applied = job.jobapplication_set.filter(resume__pk=request.user.resume.pk).exists()
    if has_applied:
        messages.warning(request, 'You have already applied for this job.')
    else:
        # Create the job application
        JobApplication.objects.create(job=job, resume=request.user.resume)
        messages.success(request, 'You have successfully applied for this job.')

    return redirect(reverse('job:all_joblist'))


def manage_appliedjobs(request):
    applied_jobs = JobApplication.objects.filter(resume=request.user.resume)
    context = {'applied_jobs': applied_jobs}
    return render(request, 'job/manage_appliedjobs.html', context)

def delete_appliedjob(request, pk):
  job_application = JobApplication.objects.get(id = pk)
  job_application.delete()
  messages.success(request,'Applied job deleted successfully')
  return redirect(reverse('job:manage_appliedjobs'))
  





    

  




