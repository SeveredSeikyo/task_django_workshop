"""
URL configuration for task_py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('login/',views.user_login,name="Login"),
    path('register/',views.register,name="Register"),
    path('dashboard/',views.dashboard,name="Dashboard"),
    path('logout/',views.user_logout,name="Logout"),
    path('create-post/',views.create_post,name="Create-Post"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset-password.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset-password-sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),name="password_reset_complete"),

]
