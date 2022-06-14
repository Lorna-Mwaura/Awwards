from django.urls import re_path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectList, basename='Projects')

urlpatterns = [
    re_path('^$',views.welcome, name="welcome"),
    re_path('register/', views.register, name ='register'),
    re_path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    re_path('profile/', views.profile, name='profile'),
    re_path('upload/', views.upload, name='upload'),
    re_path('project-api/', include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]