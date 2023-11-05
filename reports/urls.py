from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.LoginUserView.as_view(), name='login'),
]