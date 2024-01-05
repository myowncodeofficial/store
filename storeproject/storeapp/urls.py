
from django.urls import path

from storeapp import views

app_name = 'storeapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('afterlogin/', views.afterlogin, name='afterlogin'),
    path('filltheform/', views.fill_the_form, name='filltheform'),
    path('logout/', views.logout, name='logout'),
]
