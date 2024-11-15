from django.urls import path
from job import views
app_name = 'job'
urlpatterns = [
  path('create_job/', views.createjob,name='create_job'),
  path('update_job/<int:pk>/', views.update_job, name='update_job'),
  path('delete_job/<int:pk>/', views.delete_job, name='delete_job'),
  path('joblist_percomapny/', views.joblist_percompany, name='joblist_percompany'),
  path('job_detail/<int:pk>/', views.job_details, name='job_details'),
  path('add_jobresponsibility/<int:pk>/', views.add_jobresponsibility, name='add_jobresponsibility'),
  path('add_jobexperience/<int:pk>/', views.add_jobexperience, name='add_jobexperience'),
  path('delete_jobresponsibility/<int:pk>/', views.delete_jobresponsibility, name='delete_jobresponsibility'),
  path('delete_jobexperience/<int:pk>/', views.delete_jobexperience, name='delete_jobexperience'),
]
