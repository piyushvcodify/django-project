from django.contrib import admin
from django.urls import path,re_path,include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
	path('', views.apiOverview, name="api-overview"),
	path('employee-list/', views.employeeList, name="employee-list"),
	path('employee-detail/<str:pk>/', views.employeeDetail, name="employee-detail"),
	path('employee-create/', views.employeeCreate, name="employee-create"),
	path('employee-update/<str:pk>/', views.employeeUpdate, name="employee-update"),
	path('employee-delete/<str:pk>/', views.employeeDelete, name="employee-delete"),
    ]
