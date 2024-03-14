from django.urls import path
from . import views
from .views import EmployeeListView, PositionListView, DepartmentListView

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main_template, name='main_template'),
    path('search/', views.search_results, name='search_results'),
    path('employee_detail_view/<int:employee_id>/', views.employee_detail_view, name='employee_detail_view'),
    path('employee_list_view/', EmployeeListView.as_view(), name='employee_list_view'),
    path('position_list_view/', PositionListView.as_view(), name='position_list_view'),
    path('department_list_view/', DepartmentListView.as_view(), name='department_list_view'), 
    path('employee_detail_view/<int:employee_id>/add_tags_to_employee/', views.add_tags_to_employee, name='add_tags_to_employee'), 
]