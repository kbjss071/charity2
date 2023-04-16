from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('profile/<username>/', views.Profile.as_view(), name="profile")

    # path('password_change/', name="password_change"),
    # path('password_change/done', name="password_change_done"),
    # path('password_reset/', name='password_reset'),
    # path('reset/<uidb64>/<token>/', name="password_reset_confirm"),
    # path('reset/', name="password_reset_complete")
]
