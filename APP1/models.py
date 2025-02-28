from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from djmoney.models.fields import MoneyField

DepartmentList=(
    ('Human Resource','Human Resource'),
    ('Sales','Sales'),
    ('Marketing','Marketing'),
)
Role=(
    ('Manager','Manager'),
    ('Cashier','Cashier'),
    ('Admin','Admin'),
)
Resident=(
    ('Dodoma','Dodoma'),
    ('Morogora','Mogogarar'),
    ('Arusha','arusha'),
    ('Kilimanjato','Kilimanjaro')
)
states=(
    ('Indian','India'),
    ('West Bengal','West Bengal'),
    ('South affrica','South affrica'),
    ('East Coast','East coast'),
    ('Dodoma Central','Dodoma Central'),
)
Region=(
    ('Hindu','Hindu'),
    ('Muslim','Muslim'),
    ('Christin','Christan'),
)
Management=(
    ('SalesManager','SalesManager'),
    ('Customer Care Associate','Customer Care Associate'),
    ('Call Center Agent','Call Center Agent'),
    ('Help Desk Assistant','Help Desk Assistant'),
)
class Department(models.Model):
    Department=models.CharField(max_length=200,primary_key=True,choices=DepartmentList)

class Employee(models.Model):
    FULLname=models.CharField(max_length=200)
    Role=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,primary_key=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    
class Announcements(models.Model):
    Logo=models.ImageField(upload_to="Announcements/")
    Heading=models.CharField(max_length=200)
    Document=models.FileField(upload_to="Document/")
    DateRegistered=models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    Fullname=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,primary_key=True)
    Resident=models.CharField(max_length=20,choices=Resident)
    NationalID=models.CharField(max_length=200)
    States=models.CharField(max_length=200,choices=states)
    License=models.FileField(upload_to='License/')
    DateRegistered=models.DateTimeField(auto_now_add=True)
    InsuranceDuration=models.DateTimeField(auto_now_add=False)
    Construction=models.CharField(max_length=100)
    BusinessType=models.CharField(max_length=100)
    Earthquake=models.BooleanField(default=False)
    Flood=models.BooleanField(default=False)
    TINnumber=models.IntegerField(unique=True)
    About=models.TextField(blank=True,null=True)

class Compansation(models.Model):
    amount=MoneyField(max_digits=14,decimal_places=2,default_currency='TZS')
    CustomerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    RegisteredDate=models.DateTimeField(auto_now_add=True)
    BankReceipt=models.FileField(upload_to="CompasationReceipt/")  

class MonthlyInstallment(models.Model):
    amount=MoneyField(max_digits=14,decimal_places=2,default_currency='TZS')
    CustomerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    RegisteredDate=models.DateTimeField(auto_now_add=True)
    BankReceipt=models.FileField(upload_to="CompasationReceipt/")  

class Administration(models.Model):
    Role=models.CharField(max_length=200,primary_key=True,choices=Management)
    Passport=models.ImageField(upload_to="Management/")
    DateRegistered=models.DateTimeField(auto_now_add=True)
    Message=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10) 


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Add this field
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
