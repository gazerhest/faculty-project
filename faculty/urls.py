from django.urls import path
from . import views

app_name = "faculty"
urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs_list, name='programs_list'),
    path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
    path('departments/', views.departments_list, name='departments_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('exchange/', views.exchange_list, name='exchange_list'),
]
