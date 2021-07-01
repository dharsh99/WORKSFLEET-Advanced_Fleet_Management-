from django.contrib import admin
from . models import Add_Driver, Add_Fuel, Manage_Expense, Manage_Income, edit_profile1, subscribe
from . models import Admin_Registration,User_Signin_Signup,Add_User,Add_Customer,Add_New_Booking
from . models import reg_vehicle_group, reg_vehicle_type ,Add_Vendor,Add_Booking_quotation1,reg_vehicle_inspection,reg_manage_vehicle
# Register your models here.
admin.site.register(subscribe)
admin.site.register(Admin_Registration)
admin.site.register(User_Signin_Signup)
admin.site.register(Add_Driver)
admin.site.register(Add_User)
admin.site.register(Add_Customer)
admin.site.register(Manage_Income)
admin.site.register(Manage_Expense)
admin.site.register(Add_New_Booking)
admin.site.register(Add_Booking_quotation1)
admin.site.register(Add_Vendor)
admin.site.register(Add_Fuel)
admin.site.register(edit_profile1)
admin.site.register(reg_vehicle_type)
admin.site.register(reg_vehicle_group)
admin.site.register(reg_manage_vehicle)
admin.site.register(reg_vehicle_inspection)
