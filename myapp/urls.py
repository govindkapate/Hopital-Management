from django.contrib import admin
from django.urls import path,include
from.import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('list/',views.Patient_list,name='Patient_list'),
    path('create/',views.Patient_create,name='Patient_create'),
    path('update/<int:pk>',views.Patient_update,name='Patient_update'),
    path('delete/<int:pk>', views.Patient_delete, name='Patient_delete'),
    path('register/',views.register, name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'), name='login'),      
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
]
