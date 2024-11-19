from django.urls import path
from company import views
app_name = 'company'
urlpatterns = [
  path('add_company/', views.add_company,name ='add_company'),
  path('update_company/<int:pk>/', views.update_company, name='update_company'),
  path('company_detail/<int:pk>/', views.company_detail, name='company_detail'),
]
