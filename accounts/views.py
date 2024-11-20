from django.shortcuts import render, redirect, get_object_or_404
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
      return redirect('accounts:login_user')
    else:
      messages.warning(request,"Something went wrong.. Please try again later..")
      return redirect('accounts:register_candidate')
  else:
    form = UserRegisterForm()
    context = {'form': form}
  return render(request, 'accounts/register_candidate.html', context)

############################################################# REGISTER RECRUITER ########################################################
############################################################# REGISTER RECRUITER ########################################################
############################################################# REGISTER RECRUITER ########################################################

def register_recruiter(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      recruiter = form.save(commit=False)
      recruiter.is_recruiter= True
      recruiter.username = recruiter.email
      recruiter.save()
      messages.success(request, 'Account Created Successfully.. Please Login')
      return redirect('accounts:login_user')
    else:
      messages.warning(request, "Something went worng, Please try again ")
      return redirect('accounts:register_recruiter')
  else:
    form = UserRegisterForm()
    context = {'form': form}
  return render(request, 'accounts/register_recruiter.html', context)

############################################################# LOGIN USER ################################################################
############################################################# LOGIN USER ################################################################
############################################################# LOGIN USER ################################################################



def login_user(request):
    next_url = request.GET.get('next', '')  # Get the 'next' parameter if it exists

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)

            # Redirect to the next URL or the appropriate dashboard
            if next_url:
                return redirect(next_url)
            if hasattr(user, 'is_recruiter') and user.is_recruiter:
                return redirect('dashboard:dashboard_recruiter')
            elif hasattr(user, 'is_candidate') and user.is_candidate:
                return redirect('dashboard:dashboard_candidate')
            else:
                messages.error(request, "Your account type is not recognized.")
                return redirect('accounts:login_user')

        else:
            messages.warning(request, "Invalid username or password.")
            return redirect('accounts:login_user')

    return render(request, 'accounts/login.html')


############################################################# LOGOUT USER ###############################################################
############################################################# LOGOUT USER ###############################################################
############################################################# LOGOUT USER ###############################################################

def logout_user(request):
  logout(request)
  messages.success(request, "You are now logged out")
  return redirect('accounts:login_user')

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
    user = get_object_or_404(User, id=pk)  # Safer way to get the user instance
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)  # Pass POST data and files
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect(reverse('accounts:update_profile', args=[user.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please check the form and try again.')
    else:
        form = UpdateProfileForm(instance=user)  # Prepopulate form with user's existing data

    context = {'form': form}
    return render(request, 'accounts/update_profile.html', context)