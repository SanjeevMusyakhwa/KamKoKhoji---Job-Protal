from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def dashboard(request):
    if hasattr(request.user, 'is_recruiter') and request.user.is_recruiter:
        return render(request, 'dashboard/recruiter_dashboard.html')
    elif hasattr(request.user, 'is_candidate') and request.user.is_candidate:
        return render(request, 'dashboard/candidate_dashboard.html')
    else:
        # Handle the case where the user doesn't match either role
        return HttpResponseForbidden("You do not have permission to access this page.")
