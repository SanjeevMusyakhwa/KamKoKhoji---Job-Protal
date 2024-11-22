from django.urls import path
from job import views
app_name = 'job'
urlpatterns = [
  path('create_job/', views.createjob,name='create_job'),
  path('update_job/<int:pk>/', views.update_job, name='update_job'),
  path('delete_job/<int:pk>/', views.delete_job, name='delete_job'),
  path('joblist_percompany/', views.joblist_percompany, name='joblist_percompany'),
  path('job_detail/<int:pk>/', views.job_details, name='job_details'),
  path('add_jobresponsibility/<int:pk>/', views.add_jobresponsibility, name='add_jobresponsibility'),
  path('add_jobexperience/<int:pk>/', views.add_jobexperience, name='add_jobexperience'),
  path('delete_jobresponsibility/<int:pk>/', views.delete_jobresponsibility, name='delete_jobresponsibility'),
  path('delete_jobexperience/<int:pk>/', views.delete_jobexperience, name='delete_jobexperience'),
  path('aviliable_jobs/', views.all_joblist, name='all_joblist'),
  path('apply_job/<int:pk>/', views.apply_for_job, name='apply_for_job'),
  path('manage_appliedjobs/', views.manage_appliedjobs, name='manage_appliedjobs'),
  path('delete_appliedjob/<int:pk>/', views.delete_appliedjob, name='delete_appliedjob'),
]
