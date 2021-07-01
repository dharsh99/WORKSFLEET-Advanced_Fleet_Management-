from django.http import request
from django.shortcuts import render,redirect
from . models import  add_note, edit_password,Add_Fuel, Add_Vendor,Add_Booking_quotation1, Add_Customer, Add_New_Booking, Admin_Registration, Manage_Expense, edit_password, edit_profile1, subscribe,User_Signin_Signup,Add_Driver,Add_User,Manage_Income, reg_vehicle_type,reg_vehicle_group,reg_manage_vehicle,reg_vehicle_inspection
import easygui
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
import datetime

# Create your views here.
def index(request):
    return render(request,'Landing/index.html') 

def admin_login(request):
    return render(request,'Dashboard/admin_login.html')     

def admin_registration(request):
    return render(request,'Dashboard/admin_registration.html')  
 
def driver(request):
    return render(request,'Dashboard/driver.html')    

def customer(request):
    return render(request,'Dashboard/customer.html')   

def user(request):
        return render(request,'Dashboard/user.html')     

def add_driver(request):
        return render(request,'Dashboard/add_driver.html')    

def add_customer(request):
        return render(request,'Dashboard/add_customer.html')  

def add_user(request):
        return render(request,'Dashboard/add_user.html')  

def manage_vehicle(request):
        return render(request,'Dashboard/manage_vehicle.html')   

# def vehicle_group(request):
#         return render(request,'Dashboard/vehicle_group.html')   

def fuel_view(request):
        return render(request,'Dashboard/fuel_view.html')  

def manage_expense_view(request):
        return render(request,'Dashboard/manage_expense_view.html')

def add_manage_vehicle(request):
        return render(request,'Dashboard/add_manage_vehicle.html')  

# def vehicle_type(request):
#         return render(request,'Dashboard/vehicle_type.html')   

# def add_vehicle_type(request):
#         return render(request,'Dashboard/add_vehicle_type.html')      

# def driver_logs(request):
#         return render(request,'Dashboard/driver_logs.html')  

# def vehicle_inspection(request):
#         return render(request,'Dashboard/vehicle_inspection.html') 

# def add_vehicle_inspection(request):
#         return render(request,'Dashboard/add_vehicle_inspection.html')  

def manage_income_view(request):
        return render(request,'Dashboard/manage_income_view.html') 

def manage_expense_view(request):
        return render(request,'Dashboard/manage_expense_view.html')  
        
def add_manage_income(request):
        return render(request,'Dashboard/add_manage_income.html')
        
def add_manage_expense(request):
        return render(request,'Dashboard/add_manage_expense.html') 

def add_new_booking(request):
        return render(request,'Dashboard/add_new_booking.html')       
        
def manage_booking(request):
        return render(request,'Dashboard/manage_booking.html')      

def manage_booking_quotation(request):
        return render(request,'Dashboard/manage_booking_quotation.html') 
        
def add_booking_quotation(request):
        return render(request,'Dashboard/add_booking_quotation.html') 

def add_fuel(request):
        return render(request,'Dashboard/add_fuel.html')

def add_vendor(request):
        return render(request,'Dashboard/add_vendor.html') 

def manage_vendor(request):
        return render(request,'Dashboard/manage_vendor.html')

def edit_profile(request):
        return render(request,'Dashboard/edit_profile.html')   

def work_orders(request):
        return render(request,'Dashboard/work orders.html')

def note(request):
        return render(request,'Dashboard/note.html')    

def user_signin_signup(request):
        return render(request,'Dashboard/user_signin_signup.html')

def note(request):
        return render(request,'Dashboard/note.html')      

def index_subscribe(request):
        if request.method=='POST':
                subscribe_dis=subscribe(email_id=request.POST['email_id']
                                       )
                subscribe_dis.save()
                messages.success(request,"SUCCESFULLY  STORED")
                return redirect(index)
        return render(request,'Landing/index.html')

        
def Index_Admin_Login(request):
        if request.method=='POST':
                if Admin_Registration.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
                        # ex1=Admin_Registration.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
                        messages.success(request,"LOGIN SUCCESFULLY")
                        return render(request,'Dashboard/admin_login.html')
                else:
                        context={'msg':'You entered wrong username and password'}
                        return render(request,'Dashboard/admin_login.html',context)
        return render(request,'Dashboard/admin_login.html')   


def Index_Admin_Registration(request):
        if request.method=='POST':
                ex1=Admin_Registration(first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email_id=request.POST['email_id'],
                                        password=request.POST['password']
                                        )
                ex1.save()
                messages.success(request,"REGISTERED SUCCESFULLY")
                return redirect(admin_registration)   
        return render(request,'Dashboard/admin_registration.html') 

def Index_User_Login(request):
        if request.method=='POST':
                if User_Signin_Signup.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
                        ex2=User_Signin_Signup.objects.get(email=request.POST['email'],password=request.POST['password'])
                        messages.success(request,"LOGIN SUCCESFULLY")
                        return render(request,'Dashboard/User_Signin_Signup.html',{'ex2':ex2})
                else:
                        context={'msg':'You entered wrong username and password'}
                        return render(request,'Dashboard/User_Signin_Signup.html',context)
        return render(request,'Dashboard/User_Signin_Signup.html')           

def Index_User_Registration(request):
        if request.method=='POST':
                ex2=User_Signin_Signup(user_name=request.POST['user_name'],
                                            email=request.POST['email'],
                                            password=request.POST['password']
                                            )
                ex2.save()
                messages.success(request,"REGISTERED SUCCESSFULLY")
                return redirect(user_signin_signup)   
        return render(request,'Dashboard/user_signin_signup.html')                     


def index1(request):
        return render(request,'Dashboard/index1.html')
               
def logout(request):
        log(request)
        easygui.msgbox("logged out")
        return render(request,'Landing/index.html')  

def add_driver1(request):
        if request.method=='POST':
                drive=Add_Driver(first_name=request.POST['first_name'],
                                  middle_name=request.POST['middle_name'],
                                  last_name=request.POST['last_name'],
                                  assign_vehicle=request.POST['assign_vehicle'],
                                  address=request.POST['address'],
                                  email_id=request.POST['email_id'],
                                  phone_number=request.POST['phone_number'],
                                  employee_id=request.POST['employee_id'],
                                  contract_number=request.POST['contract_number'],
                                  license_number=request.POST['license_number'],
                                  issue_date=request.POST['issue_date'],
                                  expiration_date=request.POST['expiration_date'],
                                  join_date=request.POST['join_date'],
                                  leave_date=request.POST['leave_date'],
                                  password=request.POST['password'],
                                  radio=request.POST['radio'],
                                  emergency_contact_details=request.POST['emergency_contact_details']
                                )               
                if len(request.FILES) != 0:
                        drive.driver_image = request.FILES['driver_image']   
                        drive.document_file=request.FILES['document_file']
                        drive.upload_license_image=request.FILES['upload_license_image']             
                        drive.save()
                        messages.success(request,"ADDED SUCCESFULLY")
                        return redirect(add_driver)
        return render(request,'Dashboard/driver.html')

def driver(request):
        drive=Add_Driver.objects.all()
        context={'drive':drive}
        return render(request,'Dashboard/driver.html',context)            

def edit_add_driver(request,id):
        drive=Add_Driver.objects.get(id=id)
        context={'drive':drive}
        return render(request,'Dashboard/edit_add_driver.html',context)

def update_add_driver(request,id):
        drive=Add_Driver.objects.get(id=id)     
        if request.method=='POST':
                if len(request.FILES) != 0:
                        drive.driver_image = request.FILES['driver_image']    
                       
        drive.first_name=request.POST.get('first_name') 
        drive.last_name=request.POST.get('last_name')
        drive.email_id=request.POST.get('email_id')  
        drive.phone_number=request.POST.get('phone_number') 
        drive.join_date=request.POST.get('join_date') 
        drive.assign_vehicle=request.POST.get('assign_vehicle')                                       
        drive.save()
        easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
        return redirect(driver)
                           
                      
def delete_add_driver(request,id):
        drive=Add_Driver.objects.get(id=id)
        drive.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(driver)       
       
def add_user1(request):
        if request.method=='POST':
                user1=Add_User(first_name1=request.POST['first_name1'],
                              last_name=request.POST['last_name'],
                              assign_vehicle1=request.POST['assign_vehicle1'],
                              is_admin=request.POST['is_admin'],
                              permission=request.POST['permission'],
                              email_id=request.POST['email_id'],
                              phone_number=request.POST['phone_number']
                              )               
                if len(request.FILES) != 0:
                        user1.user_image = request.FILES['user_image']                 
                        user1.save()
                        messages.success(request,"ADDED SUCCESFULLY")
                        return redirect(add_user)
        return render(request,'Dashboard/user.html') 

def user(request):
        user1=Add_User.objects.all()
        context={'user1':user1}
        return render(request,'Dashboard/user.html',context)                 


def edit_add_user(request,id):
        user1=Add_User.objects.get(id=id)
        context={'user1':user1}
        return render(request,'Dashboard/edit_add_user.html',context)


def update_add_user(request,id):
        user1=Add_User.objects.get(id=id)     
        if request.method=='POST':
                if len(request.FILES) != 0:
                        user1.user_image = request.FILES['user_image']     

        user1.first_name1=request.POST.get('first_name1') 
        user1.last_name=request.POST.get('last_name') 
        user1.email_id=request.POST.get('email_id')   
                                        
        user1.save()
        easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
        return redirect(user)    

def delete_add_user(request,id):
        user1=Add_User.objects.get(id=id)
        user1.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(user)    

def add_customer1(request):
        if request.method=='POST':
                custom=Add_Customer(first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'],
                                    email_id=request.POST['email_id'],
                                    phone_number=request.POST['phone_number'],
                                    radio=request.POST['radio'],
                                    address_details=request.POST['address_details']
                                   )                         
                custom.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(add_customer)
        return render(request,'Dashboard/customer.html') 

def customer(request):
        custom=Add_Customer.objects.all()
        context={'custom':custom}
        return render(request,'Dashboard/customer.html',context)   

def edit_add_customer(request,id):
        custom=Add_Customer.objects.get(id=id)
        context={'custom':custom}
        return render(request,'Dashboard/edit_add_customer.html',context)        

def update_add_customer(request,id):
        custom=Add_Customer.objects.get(id=id)     
        if request.method=='POST':
                custom.first_name=request.POST.get('first_name') 
                custom.last_name=request.POST.get('last_name') 
                custom.email_id=request.POST.get('email_id')  
                custom.radio=request.POST.get('radio')
                custom.address_details=request.POST.get('address_details')                                    
                custom.save()
                easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
                return redirect(customer)    

def delete_add_customer(request,id):
        custom=Add_Customer.objects.get(id=id)
        custom.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(customer)    

def add_manage_income1(request):
        if request.method=='POST':
                inco=Manage_Income(select_vehicle=request.POST['select_vehicle'],
                                    income_type=request.POST['income_type'],
                                    milege=request.POST['milege'],
                                    income_date=request.POST['income_date'],
                                    income_amount=request.POST['income_amount'],
                                    total_tax=request.POST['total_tax'],
                                    total_tax_charge=request.POST['total_tax_charge'],
                                    total_amount=request.POST['total_amount'],
                                    vehicle_model=request.POST['vehicle_model'],
                                    plate=request.POST['plate'],
                                   )                         
                inco.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(manage_income_view)
        return render(request,'Dashboard/manage_income_view.html') 

def manage_income_view(request):
        inco=Manage_Income.objects.all()
        context={'inco':inco}
        return render(request,'Dashboard/manage_income_view.html',context)         
        

def edit_manage_income(request,id):
        inco=Manage_Income.objects.get(id=id)     
        context={'inco':inco}
        return render(request,'Dashboard/edit_manage_income.html',context)     

def update_manage_income(request,id):
        inco=Manage_Income.objects.get(id=id)     
        if request.method=='POST':
                inco.select_vehicle=request.POST.get('select_vehicle') 
                inco.income_type=request.POST.get('income_type') 
                inco.income_date=request.POST.get('income_date')  
                inco.income_amount=request.POST.get('income_amount')
                inco.milege=request.POST.get('milege')  
                inco.vehicle_model=request.POST.get('vehicle_model'),
                inco.plate=request.POST.get('plate'),                                  
                inco.save()
                easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
                return redirect(manage_income_view)   

def delete_manage_income(request,id):
        inco=Manage_Income.objects.get(id=id)
        inco.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(manage_income_view)                 

def add_manage_expense1(request):
        if request.method=='POST':
                expo=Manage_Expense(select_vehicle=request.POST['select_vehicle'],
                                    expense_type=request.POST['expense_type'],
                                    select_vendor=request.POST['select_vendor'],
                                    total_amount=request.POST['total_amount'],
                                    note=request.POST['note'],
                                    expense_date=request.POST['expense_date'],
                                    vehicle_model=request.POST['vehicle_model'],
                                    plate=request.POST['plate'],
                                   )                         
                expo.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(manage_expense_view)
        return render(request,'Dashboard/manage_expense_view.html') 

def manage_expense_view(request):
        expo=Manage_Expense.objects.all()
        context={'expo':expo}
        return render(request,'Dashboard/manage_expense_view.html',context)         

def edit_manage_expense(request,id):
        expo=Manage_Expense.objects.get(id=id)
        context={'expo':expo}
        return render(request,'Dashboard/edit_manage_expense.html',context)     

def update_manage_expense(request,id):
        expo=Manage_Expense.objects.get(id=id)     
        if request.method=='POST':
                expo.select_vehicle=request.POST.get('select_vehicle') 
                expo.expense_type=request.POST.get('expense_type') 
                expo.select_vendor=request.POST.get('select_vendor')
                expo.expense_date=request.POST.get('expense_date')  
                expo.total_amount=request.POST.get('total_amount')
                expo.note=request.POST.get('note')
                expo.vehicle_model=request.POST.get('vehicle_model'),
                expo.plate=request.POST.get('plate'),                                     
                expo.save()
                easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
                return redirect(manage_expense_view)   

def delete_manage_expense(request,id):
        expo=Manage_Expense.objects.get(id=id)
        expo.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(manage_expense_view) 

def add_new_booking1(request):
        if request.method=='POST':
                book=Add_New_Booking(select_customer=request.POST['select_customer'],
                                     pickup_date_time=request.POST['pickup_date_time'],
                                     dropoff_date_time=request.POST['dropoff_date_time'],
                                     select_vehicle=request.POST['select_vehicle'],
                                     select_driver=request.POST['select_driver'],
                                     num_of_travellers=request.POST['num_of_travellers'],
                                     pickup_address=request.POST['pickup_address'],
                                     dropoff_address=request.POST['dropoff_address'],
                                     notes=request.POST['notes'],
                                    
                                   )                         
                book.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(manage_booking)
        return render(request,'Dashboard/manage_booking.html') 

def manage_booking(request):
        book=Add_New_Booking.objects.all()
        context={'book':book}
        return render(request,'Dashboard/manage_booking.html',context) 

def edit_manage_booking(request,id):
        book=Add_New_Booking.objects.get(id=id)
        context={'book':book}
        return render(request,'Dashboard/edit_manage_booking.html',context)     

def update_manage_booking(request,id):
        book=Add_New_Booking.objects.get(id=id)     
        if request.method=='POST':
                book.select_customer=request.POST.get('select_customer')
                book.select_vehicle=request.POST.get('select_vehicle') 
                book.pickup_address=request.POST.get('pickup_address') 
                book.dropoff_address=request.POST.get('dropoff_address')
                book.pickup_date_time=request.POST.get('pickup_date_time')  
                book.dropoff_date_time=request.POST.get('dropoff_date_time')
                book.num_of_travellers=request.POST.get('num_of_travellers')                                    
                book.save()
                easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
                return redirect(manage_booking)   

def delete_manage_booking(request,id):
        book=Add_New_Booking.objects.get(id=id)
        book.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(manage_booking)         

def add_booking_quotation1(request):
        if request.method=='POST':
                book1=Add_Booking_quotation1(select_customer1=request.POST['select_customer1'],
                                     pickup_date_time1=request.POST['pickup_date_time1'],
                                     dropoff_date_time1=request.POST['dropoff_date_time1'],
                                     select_vehicle1=request.POST['select_vehicle1'],
                                     select_driver1=request.POST['select_driver1'],
                                     num_of_travellers1=request.POST['num_of_travellers1'],
                                     type_of_day1=request.POST['type_of_day1'],
                                     trip_milege1=request.POST['trip_milege1'],
                                     waiting_time1=request.POST['waiting_time1'],
                                     amount1=request.POST['amount1'],
                                     total_tax1=request.POST['total_tax1'],
                                     total_tax_charge1=request.POST['total_tax_charge1'],
                                     total_amount1=request.POST['total_amount1'],
                                     pickup_address1=request.POST['pickup_address1'],
                                     dropoff_address1=request.POST['dropoff_address1'],
                                     notes1=request.POST['notes1'],
                                    
                                   )                         
                book1.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(manage_booking_quotation)
        return render(request,'Dashboard/manage_booking_quotation.html')         

def manage_booking_quotation(request):
        book1=Add_Booking_quotation1.objects.all()
        context={'book1':book1}
        return render(request,'Dashboard/manage_booking_quotation.html',context)  

def edit_manage_booking_quotation(request,id):
        book1=Add_Booking_quotation1.objects.get(id=id)
        context={'book1':book1}
        return render(request,'Dashboard/edit_manage_booking_quotation.html',context)     

def update_manage_booking_quotation(request,id):
        book1=Add_Booking_quotation1.objects.get(id=id)     
        if request.method=='POST':
                book1.select_customer1=request.POST.get('select_customer1')
                book1.select_vehicle1=request.POST.get('select_vehicle1') 
                book1.pickup_address1=request.POST.get('pickup_address1') 
                book1.dropoff_address1=request.POST.get('dropoff_address1')
                book1.pickup_date_time1=request.POST.get('pickup_date_time1')  
                book1.dropoff_date_time1=request.POST.get('dropoff_date_time1')
                book1.num_of_travellers1=request.POST.get('num_of_travellers1') 
                book1.total_amount1=request.POST.get('total_amount1')                                   
                book1.save()
                easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
                return redirect(manage_booking_quotation)   

def delete_manage_booking_quotation(request,id):
        book1=Add_Booking_quotation1.objects.get(id=id)
        book1.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(manage_booking_quotation)         

def add_vendor1(request):
        if request.method=='POST':
                vend=Add_Vendor(vendor_name=request.POST['vendor_name'],
                                phone_number=request.POST['phone_number'],
                                email_id=request.POST['email_id'],
                                type=request.POST['type'],
                                website=request.POST['website'],
                                address1=request.POST['address1'],
                                address2=request.POST['address2'],
                                city=request.POST['city'],
                                state_province=request.POST['state_province'],
                                postal_code=request.POST['postal_code'],
                                country=request.POST['country'],
                                note=request.POST['note']
                              )               
                if len(request.FILES) != 0:
                        vend.vendor_image = request.FILES['vendor_image']                 
                        vend.save()
                        messages.success(request,"ADDED SUCCESFULLY")
                        return redirect(manage_vendor)
        return render(request,'Dashboard/manage_vendor.html') 

def manage_vendor(request):
        vend=Add_Vendor.objects.all()
        context={'vend':vend}
        return render(request,'Dashboard/manage_vendor.html',context)  

def edit_add_vendor(request,id):
        vend=Add_Vendor.objects.get(id=id)
        context={'vend':vend}
        return render(request,'Dashboard/edit_add_vendor.html',context)


def update_add_vendor(request,id):
        vend=Add_Vendor.objects.get(id=id)     
        if request.method=='POST':
                if len(request.FILES) != 0:
                        vend.vendor_image = request.FILES['vendor_image']     
        vend.vendor_name=request.POST.get('vendor_name') 
        vend.type=request.POST.get('type') 
        vend.phone_number=request.POST.get('phone_number')
        vend.address1=request.POST.get('address1')
        vend.email_id=request.POST.get('email_id')                                      
        vend.save()
        easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
        return redirect(manage_vendor)    

def delete_add_vendor(request,id):
        vend=Add_Vendor.objects.get(id=id)
        vend.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(manage_vendor)    

def add_fuel1(request):
        if request.method=='POST':
                fuel1=Add_Fuel(select_vehicle=request.POST['select_vehicle'],
                                date=request.POST['date'],
                                qty_gallon=request.POST['qty_gallon'],
                                start_meter=request.POST['start_meter'],
                                cost_unit=request.POST['cost_unit'],
                                reference=request.POST['reference'],
                                state_province=request.POST['state_province'],
                                note=request.POST['note']
                                )    
                if len(request.FILES) != 0:
                        fuel1.fuel_image=request.FILES['fuel_image']
                        fuel1.save()
                        messages.success(request,"ADDED SUCCESFULLY")
                        return redirect(fuel_view)
        return render(request,'Dashboard/fuel_view.html')

def fuel_view(request):
        fuel1=Add_Fuel.objects.all()
        context={'fuel1':fuel1}
        return render(request,'Dashboard/fuel_view.html',context)  

def edit_add_fuel(request,id):
        fuel1=Add_Fuel.objects.get(id=id)
        context={'fuel1':fuel1}
        return render(request,'Dashboard/edit_add_fuel.html',context)


def update_add_fuel(request,id):
        fuel1=Add_Fuel.objects.get(id=id)  
        if request.method=='POST':
                if len(request.FILES) != 0:
                        fuel1.fuel_image = request.FILES['fuel_image']       
        fuel1.select_vehicle=request.POST.get('select_vehicle')
        fuel1.date=request.POST.get('date')
        fuel1.qty_gallon=request.POST.get('qty_gallon')
        fuel1.start_meter=request.POST.get('start_meter')
        fuel1.cost_unit=request.POST.get('cost_unit')
        fuel1.reference=request.POST.get('reference')
        fuel1.state_province=request.POST.get('state_province')                                     
        fuel1.save() 
        easygui.msgbox('DATA HAS BEEN UPDATED SUCCESFULLY',title='WORKSFLEET')   
        return redirect(fuel_view)    
        
def delete_add_fuel(request,id):
        fuel1=Add_Fuel.objects.get(id=id)
        fuel1.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(fuel_view) 

def edit_profile_user(request):
        if request.method=='POST':
                pro=edit_profile1(name=request.POST['name'],
                                 email_id=request.POST['email_id'],
                                 languages=request.POST['languages']
                              )                               
                if len(request.FILES) != 0:
                        pro.profile_image = request.FILES['profile_image']                 
                        pro.save()
                        messages.success(request,"ADDED SUCCESFULLY")
                        return redirect(edit_profile)
        return render(request,'Dashboard/edit_profile.html') 

def edit_profile(request):
        pro=edit_profile1.objects.all()
        context={'pro':pro}
        return render(request,'Dashboard/edit_profile.html',context)  

def edit_password_user(request):
        if request.method=='POST':
                pas=edit_password(lock=request.POST['lock']
                                   ) 
                pas.save()
                messages.success(request,"ADDED SUCCESFULLY")
                return redirect(edit_profile)                         
        return render(request,'Dashnoard/edit_profile.html')



def reg_add_manage_vehicle(request): 
          if request.method=='POST':
             ex3=reg_manage_vehicle() 
            
             ex3.Vehicle_Type=request.POST.get('Vehicle_Type')
             ex3.Vehicle_Model=request.POST.get('Vehicle_Model')
             ex3.Vehicle_Maker=request.POST.get('Vehicle_Maker')
             ex3.Group=request.POST.get('Group')
             ex3.Color=request.POST.get('Color')
             ex3.License_Plate=request.POST.get('License_Plate')
             ex3.Assigned_Driver=request.POST.get('Assigned_Driver')
             ex3.Average_miles=request.POST.get(' Average_miles')
             ex3.license_expiry=request.POST.get('license_expiry')
             ex3.Registration_expiry=request.POST.get('Registration_expiry')
             ex3.In_service=request.POST.get('In_service')
             ex3.User_data=request.POST.get('User_data')
             ex3.Initial_milege=request.POST.get('Initial_milege')
             ex3.Vin=request.POST.get('Vin')
             ex3.Vehicle_year=request.POST.get('Vehicle_year')
            
            

             if len(request.FILES) !=0:
                ex3.Image=request.FILES['Image']

         
             ex3.save()
             messages.success(request,"ADDED SUCCESFULLY")
             return redirect(add_manage_vehicle)
          return render(request,'Dashboard/add_manage_vehicle.html')      


def manage_vehicle(request):
        view3=reg_manage_vehicle.objects.all()
        

        return render(request,'Dashboard/manage_vehicle.html',{'view3':view3})

def edit_manage_vehicle(request,id):
        view3=reg_manage_vehicle.objects.get(id=id)

        return render(request,'Dashboard/edit_manage_vehicle.html',{'view3':view3})        

def edit_manage_vehicle_update(request ,id): 
         view3=reg_manage_vehicle.objects.get(id=id) 
         if request.method=='POST':
               
             if len(request.FILES) != 0:
               
                   view3.Image=request.FILES['Image']     
           
             view3.Vehicle_Type=request.POST.get('Vehicle_Type')
             view3.Vehicle_Model=request.POST.get('Vehicle_Model')
             view3.Vehicle_Maker=request.POST.get('Vehicle_Maker')
             view3.Group=request.POST.get('Group')
             view3.Color=request.POST.get('Color')
             view3.License_Plate=request.POST.get('License_Plate')
             view3.Assigned_Driver=request.POST.get('Assigned_Driver')
             view3.Average_miles=request.POST.get('Average_miles')
             view3.license_expiry=request.POST.get('license_expiry')
             view3.Registration_expiry=request.POST.get('Registration_expiry')
       
             view3.User_data=request.POST.get('User_data')
             view3.Initial_milege=request.POST.get('Initial_milege')
             view3.Vin=request.POST.get('Vin')
             view3.Vehicle_year=request.POST.get('Vehicle_year')
            
          
             view3.save()
             easygui.msgbox("your data has been updated successfully...!",title="Worksfleet")
             return redirect(manage_vehicle)



def edit_manage_vehicle_delete(request,id):
        view3=reg_manage_vehicle.objects.get(id=id)
        view3.delete()
        messages.success(request,"DELETED SUCCESFULLY") 
        return redirect(manage_vehicle)


def add_vehicle_type(request): 
        
        return render(request,'Dashboard/add_vehicle_type.html')      




def vehicle_type(request): 
        view1=reg_vehicle_type.objects.all()
        return render(request,'Dashboard/vehicle_type.html',{'view1':view1})  


def reg_add_vehicle_type(request): 
        if request.method=='POST':
            ex1=reg_vehicle_type() 
            ex1.Vehicle_Type=request.POST.get('Vehicle_Type')
            ex1.Display_Name=request.POST.get('Display_Name')
            ex1.No_of_Seats=request.POST.get('No_of_Seats')
            

            if len(request.FILES) !=0:
                ex1.image=request.FILES['image']

         
            ex1.save()
            messages.success(request,"ADDED SUCCESFULLY")
            return redirect(vehicle_type)
        return render(request,'Dashboard/add_vehicle_type.html')      



                                               
                                                   
def edit_vehicle_type(request,id):
        
        view1=reg_vehicle_type.objects.get(id=id)
        
        
        return render(request,'Dashboard/edit_vehicle_type.html',{'view1':view1})  



def edit_vehicle_type_update(request ,id): 
        view1=reg_vehicle_type.objects.get(id=id) 
        if request.method=='POST':
           
           

            if len(request.FILES) != 0:
                # if len(view1.image) > 0:
                #     os.remove(view1.image.path)
                view1.image=request.FILES['image']

            view1.Vehicle_Type=request.POST.get('Vehicle_Type')
            view1.Display_Name=request.POST.get('Display_Name')
            view1.No_of_Seats=request.POST.get('No_of_Seats')
            
          
            view1.save()
            easygui.msgbox("your vehicle type data has been updated successfully...!",title="Worksfleet")
            return redirect(vehicle_type)


def edit_vehicle_type_delete(request,id):
        view1=reg_vehicle_type.objects.get(id=id)
        view1.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(vehicle_type)

 
def add_vehicle_group(request):
        
        return render(request,'Dashboard/add_vehicle_group.html')       
      


def reg_add_vehicle_group(request):
        if request.method =='POST':
             ex2=reg_vehicle_group(Group_Name=request.POST['Group_Name'],
                                   Description=request.POST['Description'],
                                   Note=request.POST['Note']
                                   )   
        
             ex2.save()
             messages.success(request,"ADDED SUCCESFULLY")
             return redirect(vehicle_group)
        
        return render(request,'Dashboard/add_vehicle_group.html')    
                               
                        
def vehicle_group(request):
        view2=reg_vehicle_group.objects.all()

        return render(request,'Dashboard/vehicle_group.html',{'view2':view2})  


def edit_vehicle_group(request,id):
        
        view2=reg_vehicle_group.objects.get(id=id)
        
        
        return render(request,'Dashboard/edit_vehicle_group.html',{'view2':view2})  

def edit_vehicle_group_update(request ,id): 
        view2=reg_vehicle_group.objects.get(id=id) 
        if request.method=='POST':
           
            view2.Group_Name=request.POST.get('Group_Name')
            view2.Discription=request.POST.get('Discription')
            view2.Note=request.POST.get('Note')
            
          
            view2.save()
            easygui.msgbox("your vehicle group data has been updated successfully...!",title="Worksfleet")
            return redirect(vehicle_group)



def edit_vehicle_group_delete(request,id):
        view2=reg_vehicle_group.objects.get(id=id)
        view2.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(vehicle_group)



def vehicle_inspection(request):
         view4=reg_vehicle_inspection.objects.all()
         
  


         return render(request,'Dashboard/vehicle_inspection.html',{'view4':view4})  



def add_vehicle_inspection(request):
        return render(request,'Dashboard/add_vehicle_inspection.html')  


def reg_add_vehicle_inspection(request):
          if request.method =='POST':
             ex4=reg_vehicle_inspection(Vehicle=request.POST['Vehicle'],
                                       Registration_Number=request.POST['Registration_Number'],
                                       ReviewBy=request.POST['ReviewBy'],
                                       Meter_Reading_Incoming=request.POST['Meter_Reading_Incoming'],
                                       Fuel_level_outgoing=request.POST['Fuel_level_outgoing'],
                                       Fuel_level_Incoming=request.POST['Fuel_level_Incoming'],
                                       DateTime_Outgoing=request.POST['DateTime_Outgoing'],
                                       DateTime_Incomig=request.POST['DateTime_Incomig'],
                                       Petrol_card=request.POST['Petrol_card'],
                                       Light_Indicators=request.POST['Light_Indicators'],
                                       Inventor_cigerette=request.POST['Inventor_cigerette'],
                                       Car_mats_Car_seat_covers=request.POST['Car_mats_Car_seat_covers'],
                                       Interior_damages=request.POST['Interior_damages'],
                                       Interior_Lights=request.POST['Interior_Lights'],
                                       Damagetoexterior_ofcarsdents_scratches_brokenlights_etc=request.POST['Damagetoexterior_ofcarsdents_scratches_brokenlights_etc'],
                                       TyresNew_need_replacing=request.POST['TyresNew_need_replacing'],
                                       Ladders_extension_ladder=request.POST['Ladders_extension_ladder'],
                                       Extension_leads=request.POST['Extension_leads'],
                                       Anyofour_powertools=request.POST['Anyofour_powertools'],
                                       Air_conditioner_working_or_not=request.POST['Air_conditioner_working_or_not'],
                                       Lights_headlights_working=request.POST['Lights_headlights_working'],
                                       Automaticlocks_alarmworking=request.POST['Automaticlocks_alarmworking'],
                                       Windows_working_or_not_anydamages_windowtints=request.POST['Windows_working_or_not_anydamages_windowtints'],
                                       Condition_or_carseats=request.POST['Condition_or_carseats'],
                                       oil_check=request.POST['oil_check'],
                                       Suspension=request.POST['Suspension'],
                                       Tool_boxes=request.POST['Tool_boxes']
                                      
                                      )   
        
             ex4.save()
             messages.success(request,"ADDED SUCCESFULLY")
             return redirect(vehicle_inspection)

        

          return render(request,'Dashboard/add_vehicle_inspection.html')






def edit_vehicle_inspection(request,id):

        view4=reg_vehicle_inspection.objects.get(id=id)
        return render(request,'Dashboard/edit_vehicle_inspection.html',{'view4':view4})


def edit_vehicle_inspection_update(request,id):
          view4=reg_vehicle_inspection.objects.get(id=id) 
          if request.method =='POST':
             view4.Vehicle=request.POST.get('Vehicle')
             view4.Registration_Number=request.POST.get('Registration_Number')
             view4.ReviewBy=request.POST.get('ReviewBy')
             view4.Meter_Reading_Incoming=request.POST.get('Meter_Reading_Incoming')
             view4.save()
             easygui.msgbox("your data has been updated successfully...!",title="Worksfleet")
             return redirect(vehicle_inspection)


def edit_vehicle_group_update(request ,id): 
        view2=reg_vehicle_group.objects.get(id=id) 
        if request.method=='POST':
           
            view2.Group_Name=request.POST.get('Group_Name')
            view2.Discription=request.POST.get('Discription')
            view2.Note=request.POST.get('Note')
            
          
            view2.save()
            easygui.msgbox("your vehicle group data has been updated successfully...!",title="Worksfleet")
            return redirect(vehicle_group)
        

def edit_vehicle_inspection_delete(request,id):
        view4=reg_vehicle_inspection.objects.get(id=id)
        view4.delete()
        messages.success(request,"DELETED SUCCESFULLY")
        return redirect(vehicle_inspection)



def driver_logs(request):
         view3=reg_manage_vehicle.objects.all()
         return render(request,'Dashboard/driver_logs.html',{'view3':view3})  
 


def index_note(request):
        if request.method=='POST':
                n1=add_note(content=request.POST['content'],
                                        )
                n1.save()
                messages.success(request,"REPORTED SUCCESFULLY")
                return redirect(note)   
        return render(request,'Dashboard/note.html') 
