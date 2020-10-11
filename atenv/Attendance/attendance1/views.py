from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import Employee_master,Company_master,UserLogin,User_attendance
import json
# Create your views here.
def employee_master(request):
    if UserLogin.objects.get(id=request.session['id']).permission == '2':
        data = Employee_master.objects.all()
        company_data = Company_master.objects.all()
    else:
        return redirect("attendance1:login")
    return render(request,'attendance1/employee_master.html',{'data':data, 'company_data':company_data, 'login_usr_obj': UserLogin.objects.get(id=request.session['id']), 'list_employees': Employee_master.objects.filter(emp_user_id=request.session['id'])})

def company_master(request):
    if UserLogin.objects.get(id=request.session['id']).permission == '2':
        return render(request,'attendance1/company_master.html',{'login_usr_obj': UserLogin.objects.get(id=request.session['id']), 'list_company': Company_master.objects.filter(comp_user_id=request.session['id'])})

def attendance_form(request):
    if UserLogin.objects.get(id=request.session['id']).permission == '2':
        return render(request,'attendance1/attendance_form.html',{'login_usr_obj': UserLogin.objects.get(id=request.session['id']), 'list_employees': Employee_master.objects.filter(emp_user_id=request.session['id'])})

def login(request):
    return render(request,'attendance1/login.html')

def loginform(request):
    if request.method == "POST":
        emailID = request.POST.get('email')
        password = request.POST.get('password')
        if UserLogin.objects.filter(Email=emailID).count() == 0:
            login_obj = {
                'result': "NULL"
            }

        if UserLogin.objects.filter(Email=emailID).count() > 0:
            if UserLogin.objects.filter(Email=emailID).first().Password == password:
                request.session['id'] = UserLogin.objects.filter(Email=emailID).first().id
                login_obj = {
                    'result': "EXISTS",
                }
            else:
                login_obj = {
                    'result': "NULL",
                }
    return JsonResponse(login_obj["result"],safe=False)

def post_employee_obj(request):
    if (request.method == "POST"):
        employee_name=request.POST.get('employee_name')
        comp_name= request.POST.get('employee_company')
        company_obj = Company_master.objects.get(comp_name = comp_name)
        Employee_master.objects.create(
            emp_name=employee_name,
            emp_comp_id=company_obj,
            emp_user_id=UserLogin.objects.get(id=request.session['id']),

        )
        employee_data={
            "message" : "Posted",
        }
    return JsonResponse(employee_data)

def edit_employee_obj(request):
    if (request.method) == "POST":
        employee_code = request.POST.get('employee_code')
        new_employee_name = request.POST.get('new_employee_nm')
        new_employee_company = request.POST.get('new_employee_company')
        company_obj = Company_master.objects.get(comp_name = new_employee_company)
        employee_obj = Employee_master.objects.get(emp_id = employee_code)
        employee_obj.emp_name = new_employee_name
        employee_obj.emp_comp_id = company_obj
        employee_obj.save()
        edit_employee_data = {
            "message": "edited",
        }
    return JsonResponse(edit_employee_data)

def delete_employee_obj(request):
    if (request.method) == "POST":
        employee_code = request.POST.get('employee_code')
        delete_inst = Employee_master.objects.get(emp_id=employee_code)
        delete_inst.delete()

        delete_employee_data = {
            "message": "deleted",
        }
    return JsonResponse(delete_employee_data)

def post_company_obj(request):
    if (request.method == "POST"):
        cp_name=request.POST.get('company_name')
        Company_master.objects.create(
            comp_name=cp_name,
            comp_user_id=UserLogin.objects.get(id=request.session['id']),
        )
        company_data={
            "message" : "Posted",
        }
        return JsonResponse(company_data)

def edit_company_obj(request):
    if (request.method) == "POST":
        company_code = request.POST.get('cp_code')
        new_cp_name = request.POST.get('new_cp_nm')
        company_obj = Company_master.objects.get(comp_id=company_code)
        company_obj.comp_name = new_cp_name
        company_obj.save()
        edit_company_data = {
            "message": "edited",
        }
        return JsonResponse(edit_company_data)

def delete_company_obj(request):
    if (request.method) == "POST":
        cp_code = request.POST.get('cp_code')
        delete_inst = Company_master.objects.get(comp_id=cp_code)
        delete_inst.delete()

        delete_company_data = {
            "message": "deleted",
        }
        return JsonResponse(delete_company_data)

def add_attendance(request):
    if(request.method) == "POST":
        employee_ids = json.loads(request.POST.get('emp_ids'))
        attendance = json.loads(request.POST.get('attendance'))
        list0 = []
        list1 = employee_ids
        list2 = attendance
        list3 = []
        for j in list1:
            emp_id_obj = Employee_master.objects.get()
        print(list1)
        print(list2)
        for i in list1, list2:
            var1 = User_attendance(ua_emp_id=i, attendance=i)
            list0.append(var1)
        print(list0)
        return JsonResponse(list1,safe=False)

def Logout(request):
    try:
        del request.session['id']
        return redirect("/")
    except:
        return redirect("attendance1:login")