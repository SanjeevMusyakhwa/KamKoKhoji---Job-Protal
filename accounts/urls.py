from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
  path('register_candidate/', views.register_candidate,name ='register_candidate'),
  path('register_recuriter/', views.register_recruiter, name='register_recruiter'),
  path('login_user/', views.login_user, name='login_user'),
  path('logout/', views.logout_user, name='logout_user'),
  path('change_password/', views.change_password, name='change_password'),
  path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
]
