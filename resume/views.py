from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

def add_resume(request):
  if request.method == 'POST':
    form = CreateResumeForm(request.POST)
    if form.is_valid:
      resume = form.save(commit = False)
      resume.user = request.user
      user = User.objects.get(id = request.user.pk)
      user.has_resume = True
      resume.save()
      user.save()
      messages.success(request, "You have added your resume")
      return redirect(reverse('resume:resume_details', args= [resume.pk]))
    else:
      messages.warning(request,'Something went wrong')
      return redirect(reverse('resume:add_resume', args= [resume.pk]))
  else:
    form = CreateResumeForm()
    context = {'form': form}
  return render(request,'resume/add_resume.html', context)

def update_resume(request, pk):
  resume = Resume.objects.get(id =pk)
  if request.method == 'POST':
    form = UpdateResumeForm(request.POST, instance=resume)
    if form.is_valid():
      form.save()
      messages.success(request, 'Resume has been updated successfully')
      return redirect(reverse('resume:resume_details'))
    else:
      messages.warning(request,'Something went wrong')
      return redirect(reverse('resume:update_resume'))
  else:
    form = UpdateResumeForm(instance=resume)
    context = {'form': form}
  return render(request, 'resume/update_resume.html', context)





def resume_details(request, pk):
  resume = Resume.objects.get(id = pk)
  education = resume.education_set.all()
  work = resume.work_set.all()
  context ={'resume':resume, 'education':education, 'work':work}
  return render(request,'resume/resume_details.html', context)

def add_education(request, pk):
  resume = Resume.objects.get(id = pk)
  if request.method == 'POST':
    form = AddEducationForm(request.POST)
    if form.is_valid():
      education = form.save(commit=False)
      education.resume = resume
      education.save()
      messages.success(request, 'Education added in the resume')
      return redirect(reverse('resume:add_education', args=[resume.pk]))
    else:
      messages.warning(request,'Something went wrong')
      return redirect(reverse('resume:add_education', args=[resume.pk]))
  else:
    form = AddEducationForm()
    context = {'form': form}
  return render(request, 'resume:add_education.html', context)

def update_education(request, pk):
  education = Education.objects.get(id = pk)
  if request.method == 'POST':
    form = UpdateEducationForm(request.POST, instance=education)
    if form.is_valid():
      form.save()
      messages.success(request, 'Education Has been updated')
      return redirect(reverse('resume:Eduaction_details', args=[education.pk]))
    else:
      messages.warning(request, 'Something Went Wrong')
      return redirect(reverse('resume:update_resume', args=[education.pk]))
  else:
    form = UpdateEducationForm(instance=education)
    context = {'form': form}
  return render(request, 'resume/update_education.html', context)

def delete_education(request, pk):
  education = Education.objects.get(id = pk)
  resume = Resume.objects.get(pk = education.resume.pk)
  education.delete()
  messages.success(request, "Education Deleted Successfully")
  return redirect(reverse('resume:resume_details', args=[resume.pk]))

def add_work(request, pk):
  resume = Resume.objects.get(id = pk)
  if request.method == 'POST':
    form = AddWorkForm(request.POST)
    if form.is_valid():
      work = form.save(commit=False)
      work.resume = resume
      work.save()
      messages.success(request, 'Work has Been added to resume')
      return redirect(reverse('resume:add_work', args=[resume.pk]))
    else:
      messages.warning(request,'Something Went Worng')
      return redirect(reverse('resume:add_work', args=[resume.pk]))
  else:
    form = AddWorkForm()
    context = {'form': form}
  return render(request, 'resume/add_work.html', context)


def update_work(request, pk):
  work = Work.objects.get(id = pk)
  if request.method == 'POST':
    form = UpdateWorkForm(request.POST, instance=work)
    if form.is_valid():
      form.save()
      messages.success(request, 'Work Has been updated')
      return redirect(reverse('resume:update_work', args=[work.pk]))
    else:
      messages.warning(request, 'Something went worng')
      return redirect(reverse('resume:update_work', args=[work.pk]))
  else:
    form = UpdateWorkForm(instance = work)
    context = {'form': form}
  return render(request,'resume/update_work.html', context)

def delete_work(request, pk):
  work = Work.objects.get(id = pk)
  resume = Resume.objects.get(pk = work.resume.pk)
  work.delete()
  messages.success(request, "Work Deleted Successfully")
  return redirect(reverse('resume:resume_details', args=[resume.pk]))


