from app_users import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('log_out/', views.user_logout, name='logout'),
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('gate/', views.display_widgets, name='gate'),
    path('dashboard/', views.dashboard, name='workspace'),
]
