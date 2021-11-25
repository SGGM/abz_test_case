from django.shortcuts import render

from .models import Employee



def show_employees(request):
    context = {'employees': Employee.objects.all()}
    return render(request, "employee_hierarchy/employees.html", context)
