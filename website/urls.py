from django.urls import path
from website import views
app_name = 'website'
urlpatterns = [
  path('', views.HomePage,name ='home'),
  
 
]
