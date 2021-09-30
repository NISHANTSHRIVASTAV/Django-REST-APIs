from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_employee/', views.get_employee),
    path('insert_employee/',views.insert_employee),
    path('update_employee/', views.update_employee),
    path('delete_employee/', views.delete_employee),
]
