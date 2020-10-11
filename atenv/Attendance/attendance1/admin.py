from django.contrib import admin
from .models import Employee_master,User_attendance,UserLogin,Company_master
# Register your models here.
admin.site.register(Employee_master)
admin.site.register(Company_master)
admin.site.register(UserLogin)
admin.site.register(User_attendance)