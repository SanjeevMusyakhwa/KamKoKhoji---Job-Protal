from django.shortcuts import render, redirect, get_object_or_404
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
        if form.is_valid():
            # If the form is valid, save the resume and link to the user
            resume = form.save(commit=False)
            resume.user = request.user
            user = User.objects.get(id=request.user.pk)
            user.has_resume = True
            resume.save()
            user.save()
            messages.success(request, "You have added your resume")
            return redirect(reverse('resume:resume_details', args=[resume.pk]))
        else:
            # If the form is not valid, show a warning message and re-render the form
            messages.warning(request, 'Something went wrong. Please check the form.')
            return render(request, 'resume/add_resume.html', {'form': form})
    else:
        # If the request is not POST, just create an empty form
        form = CreateResumeForm()

    return render(request, 'resume/add_resume.html', {'form': form})


def update_resume(request, pk):
  resume = Resume.objects.get(id =pk)
  if request.method == 'POST':
    form = UpdateResumeForm(request.POST, instance=resume)
    if form.is_valid():
      form.save()
      messages.success(request, 'Resume has been updated successfully')
      return redirect(reverse('resume:resume_details' ,args=[resume.pk]))
    else:
      messages.warning(request,'Something went wrong')
      return redirect(reverse('resume:update_resume', args=[resume.pk]))
  else:
    form = UpdateResumeForm(instance=resume)
    context = {'form': form}
  return render(request, 'resume/update_resume.html', context)





def resume_details(request, pk):
  resume = Resume.objects.get(id = pk)
  education = resume.educations.all().order_by("-end_year")
  work = resume.work_experiences.all().order_by("-end_year")
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
  return render(request, 'resume/add_education.html', context)

def update_education(request, pk):
    education = get_object_or_404(Education, id=pk)  # Improved handling
    resume = education.resume

    if request.method == 'POST':
        form = UpdateEducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education has been updated successfully!')
            return redirect(reverse('resume:resume_details', args=[resume.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
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

def add_experience(request, pk):
  resume = Resume.objects.get(id = pk)
  if request.method == 'POST':
    form = AddExperienceForm(request.POST)
    if form.is_valid():
      work = form.save(commit=False)
      work.resume = resume
      work.save()
      messages.success(request, 'Experience has been added to your Resume')
      return redirect(reverse('resume:add_experience', args=[resume.pk]))
    else:
      messages.warning(request,'Something Went Worng')
      return redirect(reverse('resume:add_experience', args=[resume.pk]))
  else:
    form = AddExperienceForm()
    context = {'form': form}
  return render(request, 'resume/add_experience.html', context)


def update_experience(request, pk):
    experience = get_object_or_404(Work, id=pk)  # Ensure proper error handling
    if request.method == 'POST':
        form = UpdateExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience has been updated successfully to your Resume!')
            return redirect(reverse('resume:resume_details', args=[experience.resume.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
    else:
        form = UpdateExperienceForm(instance=experience)

    context = {'form': form}
    return render(request, 'resume/update_experience.html', context)

def delete_experience(request, pk):
  work = Work.objects.get(id = pk)
  resume = Resume.objects.get(pk = work.resume.pk)
  work.delete()
  messages.success(request, "Experience Deleted Successfully")
  return redirect(reverse('resume:resume_details', args=[resume.pk]))


