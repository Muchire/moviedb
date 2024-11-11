from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard/', views.movie, name='movie'),
  path('login/',views.login_view,name='login'),
  path('signup/', views.auth_view, name='authView'),
  path("accounts/", include("django.contrib.auth.urls")),
  path('logout/', LogoutView.as_view(), name='logout'),
] 