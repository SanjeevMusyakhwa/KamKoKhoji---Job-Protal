from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
  if request.user.is_recruiter:
    return render(request, 'dashboard/recruiter_dashboard')
  elif request.user.is_candidate:
    return render(request,'dashboard/candidate_dashboard' )
