from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views


urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name = 'login'),
	path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('register/', user_views.user_register, name='register'),
    path('profile/', user_views.profile, name = 'profile')

]
