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
  path('add_work/<int:pk>/', views.add_work, name='add_work'),
  path('update_work/<int:pk>/', views.update_work, name='update_work'),
  path('delete_work/<int:pk>/', views.delete_work, name='delete_work'),
]
