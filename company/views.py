from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

def add_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            try:
                user = User.objects.get(pk=request.user.pk)
                user.has_company = True
                company.save()
                user.save()
                messages.success(request, "Company has been added, Please create a job")
                return redirect('dashboard:dashboard_recruiter')
            except User.DoesNotExist:
                messages.warning(request, "User not found. Please try again later.")
                return redirect('company:add_company')
        else:
            messages.warning(request, "Something went wrong. Please try again later.")
            return redirect('company:add_company')
    else:
        form = AddCompanyForm()
        context = {'form': form}
        return render(request, 'company/add_company.html', context)

def update_company(request, pk): 
  company = Company.objects.get(id = pk)
  if request.method == 'POST':
    form = UpdateComapnyForm(request.POST, instance=company)
    if form.is_valid():
      form.save()
      messages.success(request, "Your company has been updated and saved..")
      return redirect(reverse('company:company_detail'))
    else:
      messages.warning(request, 'Something went wrong..., Please Try again later')
      return redirect(reverse('company:company_detail'))
  else:
    form = UpdateComapnyForm()
    context = {'form': form}
  return render(request,'company/update_company.html', context)


def company_detail(request, pk):
  company = Company.objects.get(id = pk)
  context = {'company': company}
  return render(request, 'company/company_detail.html', context)

  