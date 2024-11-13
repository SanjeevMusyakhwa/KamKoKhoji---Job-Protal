from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
# Create your views here.
from .forms import *

User = get_user_model()

############################################################# REGISTER CANDIDATE ########################################################
############################################################# REGISTER CANDIDATE ########################################################
############################################################# REGISTER CANDIDATE ########################################################

def register_candidate(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_candidate = True
      user.username = user.email
      user.save()
      messages.success(request, "Account Created Successfully.. Please Login..")
      return redirect('accounts:login')
    else:
      messages.warning(request,"Something went wrong.. Please try again later..")
      return redirect('accounts:register_candidtae')
  else:
    form = UserRegisterForm
    context = {'form': form}
  return render(request, 'accounts/register_candidate.html', context)

############################################################# REGISTER RECRUITER ########################################################
############################################################# REGISTER RECRUITER ########################################################
############################################################# REGISTER RECRUITER ########################################################

def register_recruiter(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      recruiter = form.save(commit=False)
      recruiter.is_recruiter= True
      recruiter.username = recruiter.email
      recruiter.save()
      messages.success(request, 'Account Created Successfully.. Please Login')
      return redirect('accounts:login')
    else:
      messages.warning(request, "Something went worng, Please try again ")
      return redirect('accounts:register_recruiter')
  else:
    form = UserRegisterForm
    context = {'form': form}
  return render('request', 'accounts/register_recruiter.html', context)

############################################################# LOGIN USER ################################################################
############################################################# LOGIN USER ################################################################
############################################################# LOGIN USER ################################################################

def login_user(request):
  next = ''
  if request.GET:
    next = request.GET['next']
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)

    if user is not None and user.is_active:
      login(request, user)
      if next == '':
        return redirect('dashboard')
      else:
        return redirect(next)
    else:
      messages.warning(request, 'Something Went Wrong. Please try again later')
      return redirect('accounts:login')
  return render(request, 'accounts/login.html')

############################################################# LOGOUT USER ###############################################################
############################################################# LOGOUT USER ###############################################################
############################################################# LOGOUT USER ###############################################################

def logout_user(request):
  logout(request)
  messages.success(request, "You are now logged out")
  return redirect('accounts:login')

############################################################# CHANGE PASSOWRD ###########################################################
############################################################# CHANGE PASSOWRD ###########################################################
############################################################# CHANGE PASSOWRD ###########################################################

def change_password(request):
  if request.method == 'POST':
    form = UserPasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request, 'Your password has been changed..')
      return redirect('accounts:dashboard')
    else:
      messages.error(request,"Something went wrong")
  else:
    form = UserPasswordChangeForm(request.user)
    context = {'form': form}
  return render(request, 'accounts/password_change.html', context)

############################################################# UPDATE PASSWORD ###########################################################
############################################################# UPDATE PASSWORD ###########################################################
############################################################# UPDATE PASSWORD ###########################################################

def update_profile(request, pk):
  user = User.objects.get(id = pk)
  if request.method == 'POST':
    form =  UpdateProfileForm(request.user, instance = user)
    if form.is_valid():
      form.save()
      messages.success('request', 'Your Profile has been updated.....')
      return redirect(reverse('update_profile', args= [user.pk]))
    else:
      messages.warning(request, 'Something went Wrong')
      return redirect(reverse('update_profile', args= [user.pk]))
  else:
    form = UpdateProfileForm()
    context = {'form': form}
  return render(request, 'accounts/update_profile.html',context)