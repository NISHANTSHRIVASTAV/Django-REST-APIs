from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_employee/', views.EmployeeAPI.as_view()),
    path('insert_employee/',views.EmployeeAPI.as_view()),
    path('update_employee/', views.EmployeeAPI.as_view()),
    path('delete_employee/', views.EmployeeAPI.as_view()),
]
