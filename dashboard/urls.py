from django.urls import path
from dashboard import views
app_name = 'dashboard'
urlpatterns = [
  path('dashboard_candidate/', views.dashboard,name ='dashboard_candidate'),
  path('dashboard_recruiter/', views.dashboard, name='dashboard_recruiter'),
]
