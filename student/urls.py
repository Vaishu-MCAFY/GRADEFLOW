from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('student/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<str:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),

    path('analytics/', views.analytics, name='analytics'),

path("upload/", views.upload_csv, name="upload_csv"),
    path('api/student/', views.student_api, name='student_api'),
    
]