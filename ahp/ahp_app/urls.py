from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('ahp_calculator/', views.ahp_calculator),
    path('user/', views.user),
    path('login/', views.login),
    path('register/', views.register)
]



