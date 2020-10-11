from django.db import models

# Create your models here.

class UserLogin(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    permission = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Email)

class Company_master(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_user_id = models.ForeignKey(UserLogin,on_delete=models.CASCADE, null=True)
    comp_name = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return str(self.comp_name)

class Employee_master(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100, null=True, blank=True)
    emp_comp_id = models.ForeignKey(Company_master,on_delete=models.CASCADE,null=True)
    emp_user_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.emp_name)

class User_attendance(models.Model):
    user_att_id = models.AutoField(primary_key=True)
    ua_emp_id = models.ForeignKey(Employee_master,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    attendance = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return str(self.ua_emp_id)