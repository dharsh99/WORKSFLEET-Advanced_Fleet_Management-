from django.db import models
from django.db.models.fields import CharField

from django.db.models.fields import FilePathField 
import os

import datetime


# Create your models here.
class subscribe(models.Model):
    email_id=models.EmailField()
    
    def __str__(self):
        return self.email_id

class Admin_Registration(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class User_Signin_Signup(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name  

class Add_Driver(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100) 
    assign_vehicle = models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.IntegerField()
    employee_id=models.IntegerField()
    contract_number=models.IntegerField()
    license_number=models.IntegerField()
    issue_date=models.DateField(blank=False, null=True)
    expiration_date=models.DateField(blank=False, null=True)
    join_date=models.DateField(blank=False, null=True)
    leave_date=models.DateField(blank=False, null=True)
    password=models.CharField(max_length=100)
    radio=models.CharField(max_length=100)
    radio=models.CharField(max_length=100)
    emergency_contact_details=models.CharField(max_length=100)
    driver_image=models.ImageField(upload_to='driver_image/%Y/%m/%d',null=True,blank=True)
    document_file=models.FileField(upload_to='document_file/%Y/%m/%d',null=True,blank=True)
    upload_license_image=models.ImageField(upload_to='upload_license_image/%Y/%m/%d',null=True,blank=True)
  

    def __str__(self):
        return self.first_name 
          
class Add_User(models.Model):
    first_name1=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.IntegerField()
    is_admin=models.CharField(max_length=100)
    permission=models.CharField(max_length=100)
    assign_vehicle1=models.CharField(max_length=100)
    user_image=models.ImageField(upload_to='user_image/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
       return self.first_name1    

class Add_Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email_id=models.EmailField()
    radio=models.CharField(max_length=100)
    address_details=models.CharField(max_length=100)


    def __str__(self):
       return self.first_name   

class Manage_Income(models.Model):
    select_vehicle=models.CharField(max_length=100)
    income_type=models.CharField(max_length=100)
    milege=models.CharField(max_length=100)
    income_date=models.DateField(max_length=100)
    income_amount=models.CharField(max_length=100)
    total_tax=models.CharField(max_length=100)
    total_tax_charge=models.CharField(max_length=100)
    total_amount=models.CharField(max_length=100)
    vehicle_model=models.CharField(max_length=100)
    plate=models.CharField(max_length=100)
    
   
    def __str__(self):
       return self.select_vehicle   

class Manage_Expense(models.Model):
    select_vehicle=models.CharField(max_length=100)
    expense_type=models.CharField(max_length=100)
    select_vendor=models.CharField(max_length=100)
    total_amount=models.IntegerField()
    note=models.CharField(max_length=100)
    expense_date=models.DateField()
    vehicle_model=models.CharField(max_length=100)
    plate=models.CharField(max_length=100)

    def __str__(self):
        return self.select_vehicle       

class Add_New_Booking(models.Model):
    select_customer=models.CharField(max_length=100)
    select_vehicle=models.CharField(max_length=100) 
    pickup_date_time=models.CharField(max_length=100)
    dropoff_date_time=models.CharField(max_length=100)
    select_driver=models.CharField(max_length=100)
    num_of_travellers=models.CharField(max_length=100)
    pickup_address=models.CharField(max_length=100)
    dropoff_address=models.CharField(max_length=100)
    notes=models.CharField(max_length=100)

    def __str__(self):
       return self.select_customer 

class Add_Booking_quotation1(models.Model):
    select_customer1=models.CharField(max_length=100)
    select_vehicle1=models.CharField(max_length=100) 
    pickup_date_time1=models.CharField(max_length=100)
    dropoff_date_time1=models.CharField(max_length=100)
    select_driver1=models.CharField(max_length=100)
    num_of_travellers1=models.CharField(max_length=100)
    type_of_day1=models.CharField(max_length=100)
    trip_milege1=models.CharField(max_length=100)
    waiting_time1=models.CharField(max_length=100)
    amount1=models.IntegerField()
    total_tax1=models.IntegerField()
    total_tax_charge1=models.IntegerField()
    total_amount1=models.IntegerField()
    pickup_address1=models.CharField(max_length=100)
    dropoff_address1=models.CharField(max_length=100)
    notes1=models.CharField(max_length=100)
  

    def __str__(self):
        return self.select_customer1 

class Add_Vendor(models.Model):
    vendor_image=models.ImageField(upload_to='vendor_image/%Y/%m/%d',null=True,blank=True)
    vendor_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email_id=models.EmailField()
    type=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)  
    state_province=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name

class Add_Fuel(models.Model):
    select_vehicle=models.CharField(max_length=100)
    fuel_tank=models.CharField(max_length=100)
    fuel_tank1=models.CharField(max_length=100)
    vendor=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    qty_gallon=models.CharField(max_length=100)
    start_meter=models.CharField(max_length=100)
    cost_unit=models.CharField(max_length=100)
    reference=models.CharField(max_length=100)
    state_province=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    fuel_image=models.ImageField(upload_to='fuel_image/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
      return self.select_vehicle   

class edit_profile1(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profile_image/%Y/%m/%d',null=True,blank=True)
    languages=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class edit_password(models.Model):
    lock=models.CharField(max_length=100)

    





from django.db.models.fields import FilePathField 

class reg_vehicle_type(models.Model):
    Vehicle_Type=models.CharField(max_length=100)
    Display_Name=models.CharField(max_length=100)
    No_of_Seats=models.CharField(max_length=100) 
    image=models.ImageField(upload_to='filepath', null=True, blank=True)
  

    def __str__(self):
        return self.Vehicle_Type
    

class reg_vehicle_group(models.Model):
    Group_Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Note=models.CharField(max_length=500)
    Is_Enable=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Group_Name 



class reg_manage_vehicle(models.Model):
    Vehicle_Maker=models.CharField(max_length=100)
    Vehicle_Model=models.CharField(max_length=100)
    Vehicle_Type=models.CharField(max_length=100)
    Color=models.CharField(max_length=100)
    License_Plate=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='filepath', null=True, blank=True)
    Assigned_Driver=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Average_miles=models.IntegerField(blank=False, null=True)
    license_expiry=models.DateField(blank=False, null=True)
    Registration_expiry=models.DateField(blank=False, null=True)
    In_service=models.CharField(max_length=100)
    User_data=models.CharField(max_length=200)
    Initial_milege=models.CharField(max_length=100)
    Vin=models.CharField(max_length=100)
    Vehicle_year=models.DateField(blank=False, null=True)
 


    





    def __str__(self):
        return self.Vehicle_Maker



class reg_vehicle_inspection(models.Model):
    Vehicle=models.CharField(max_length=100)
    Registration_Number=models.CharField(max_length=100)
    ReviewBy=models.CharField(max_length=100)
    Meter_Reading_Incoming=models.CharField(max_length=100)
    Fuel_level_outgoing=models.CharField(max_length=100)
    Fuel_level_Incoming=models.CharField(max_length=100)
    DateTime_Outgoing=models.DateTimeField(blank=False, null=True)
    DateTime_Incomig=models.DateTimeField(blank=False, null=True)
    Petrol_card=models.CharField(max_length=100)
    Light_Indicators=models.CharField(max_length=100)
    Inventor_cigerette=models.CharField(max_length=100)
    Car_mats_Car_seat_covers=models.CharField(max_length=100)
    Interior_damages=models.CharField(max_length=100)
    Interior_Lights=models.CharField(max_length=100)
    Damagetoexterior_ofcarsdents_scratches_brokenlights_etc=models.CharField(max_length=100)
    TyresNew_need_replacing=models.CharField(max_length=100)
    Ladders_extension_ladder=models.CharField(max_length=100)
    Extension_leads=models.CharField(max_length=100)
    Anyofour_powertools=models.CharField(max_length=100)
    Air_conditioner_working_or_not=models.CharField(max_length=100)
    Lights_headlights_working=models.CharField(max_length=100)
    Automaticlocks_alarmworking=models.CharField(max_length=100)
    Windows_working_or_not_anydamages_windowtints=models.CharField(max_length=100)
    Condition_or_carseats=models.CharField(max_length=100)
    oil_check=models.CharField(max_length=100)
    Suspension=models.CharField(max_length=100)
    Tool_boxes=models.CharField(max_length=100)

    
    

    def __str__(self):
        return self.Vehicle

class add_note(models.Model):
    content=models.CharField(max_length=100)

    def __str__(self):
        return self.content

