from django.urls import path
from resume import views
app_name = 'resume'
urlpatterns = [
  path('add_resume/', views.add_resume,name ='add_resume'),
  path('update_resume/<int:pk>/', views.update_resume, name='update_resume'),
  path('resume_details/<int:pk>/', views.resume_details, name='resume_details'),
  path('add_education/<int:pk>/', views.add_education, name='add_education'),
  path('update_education/<int:pk>/', views.update_education, name='update_education'),
  path('delete_education/<int:pk>/', views.delete_education, name='delete_education'),
  path('add_experience/<int:pk>/', views.add_experience, name='add_experience'),
  path('update_experience/<int:pk>/', views.update_experience, name='update_experience'),
  path('delete_experience/<int:pk>/', views.delete_experience, name='delete_experience'),
  path('add_skill/<int:pk>/', views.add_skill, name='add_skill'),
  path('update_skill/<int:pk>/', views.update_skill, name='update_skill'),
  path('delete_skill/<int:pk>/', views.delete_skill, name='delete_skill'),
]
