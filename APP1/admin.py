from django.contrib import admin
from .import models

class EmployeeAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('FULLname','Role','Email','Department')
admin.site.register(models.Employee,EmployeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('Department',)
admin.site.register(models.Department,DepartmentAdmin)

class AdministrationAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('Role','Passport','Message','Phone')
admin.site.register(models.Administration,AdministrationAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('Heading','Document','DateRegistered')
admin.site.register(models.Announcements,AnnouncementAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('Fullname','Email','Resident','NationalID','States','License','Construction','BusinessType','Earthquake','Flood','TINnumber')
admin.site.register(models.Customer,CustomerAdmin)
 
class CompansationAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('amount','CustomerID','RegisteredDate','BankReceipt')
admin.site.register(models.Compansation,CompansationAdmin)
 
class MonthlyInstallmentAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('amount','CustomerID','RegisteredDate','BankReceipt')
admin.site.register(models.MonthlyInstallment,MonthlyInstallmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_per_page=4
    list_max_show_all=6
    list_display=('name','email','phone','message')
admin.site.register(models.Contact,ContactAdmin)
