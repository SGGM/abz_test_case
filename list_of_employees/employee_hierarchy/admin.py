from django.contrib import admin

from .models import Employee



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'position',
                    'employment_date', 'salary', 'parent')


admin.site.register(Employee, EmployeeAdmin)
