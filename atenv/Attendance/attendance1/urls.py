from django.conf.urls import url,include
from . import views

app_name = "attendance1"

urlpatterns=[
    url(r'^login/loginform', views.loginform, name='loginform'),
    url(r'^login', views.login, name='login'),
    url(r'^employee_master/post_employee_obj', views.post_employee_obj, name='post_employee_obj'),
    url(r'^employee_master/edit_employee_obj', views.edit_employee_obj, name='edit_employee_obj'),
    url(r'^employee_master/delete_employee_obj', views.delete_employee_obj, name='delete_employee_obj'),
    url(r'^company_master/post_company_obj', views.post_company_obj, name='post_company_obj'),
    url(r'^company_master/edit_company_obj', views.edit_company_obj, name='edit_company_obj'),
    url(r'^company_master/delete_company_obj', views.delete_company_obj, name='delete_company_obj'),
    url(r'^attendance_form/add_attendance', views.add_attendance, name='add_attendance'),
    url(r'^Logout', views.Logout, name='Logout'),
    url(r'^employee_master', views.employee_master, name='employee_master'),
    url(r'^company_master', views.company_master, name='company_master'),
    url(r'^attendance_form', views.attendance_form, name='attendance_form'),

]