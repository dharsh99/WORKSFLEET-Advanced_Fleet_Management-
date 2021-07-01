from django.urls import path
from . import views

# devarajuuuuu....start
import os
from django.conf import settings
from django.conf.urls.static import static
# devarajuuuu...end

urlpatterns=[
    path('',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_registration',views.admin_registration,name='admin_registration'),
    path('index1',views.index1,name='index1'),
    path('driver',views.driver,name='driver'),
    path('customer',views.customer,name='customer'),
    path('user',views.user,name='user'),
    path('add_driver',views.add_driver,name='add_driver'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('add_user',views.add_user,name='add_user'),
    path('manage_vehicle',views.manage_vehicle,name='manage_vehicle'),
    path('vehicle_group',views.vehicle_group,name='vehicle_group'),
    path('manage_expense_view',views.manage_expense_view,name='manage_expense_view'),
    path('add_manage_vehicle',views.add_manage_vehicle,name='add_manage_vehicle'),
    path('vehicle_type',views.vehicle_type,name='vehicle_type'),
    path('add_vehicle_type',views.add_vehicle_type,name='add_vehicle_type'),
    path('driver_logs',views.driver_logs,name='driver_logs'),
    path('vehicle_inspection',views.vehicle_inspection,name='vehicle_inspection'),
    path('add_vehicle_inspection',views.add_vehicle_inspection,name='add_vehicle_inspection'),
    path('manage_income_view',views.manage_income_view,name='manage_income_view'),
    path('manage_expense_view',views.manage_expense_view,name='manage_expense_view'),
    path('add_manage_income',views.add_manage_income,name='add_manage_income'),
    path('add_manage_expense',views.add_manage_expense,name='add_manage_expense'),
    path('add_new_booking',views.add_new_booking,name='add_new_booking'),
    path('manage_booking',views.manage_booking,name='manage_booking'),
    path('manage_booking_quotation',views.manage_booking_quotation,name='manage_booking_quotation'),
    path('add_booking_quotation',views.add_booking_quotation,name='add_booking_quotation'),
    path('fuel_view',views.fuel_view,name='fuel_view'),
    path('add_fuel',views.add_fuel,name='add_fuel'),
    path('add_vendor',views.add_vendor,name='add_vendor'),
    path('manage_vendor',views.manage_vendor,name='manage_vendor'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('work_orders',views.work_orders,name='work_orders'),
    path('note',views.note,name='note'),
    path('user_signin_signup',views.user_signin_signup,name='user_signin_signup'),
    path('index_subscribe',views.index_subscribe,name='index_subscribe'),
    path('Index_Admin_Registration',views.Index_Admin_Registration,name='Index_Admin_Registration'),
    path('Index_Admin_Login',views.Index_Admin_Login,name='Index_Admin_Login'),
    path('Index_User_Registration',views.Index_User_Registration,name='Index_User_Registration'),
    path('Index_User_Login',views.Index_User_Login,name='Index_User_Login'),
    path('logout',views.logout,name='logout'),
    path('add_driver1',views.add_driver1,name='add_driver1'),
    path('edit_add_driver/<int:id>',views.edit_add_driver,name='edit_add_driver'),
    path('update_add_driver/<int:id>',views.update_add_driver,name='update_add_driver'),
    path('delete_add_driver/<int:id>',views.delete_add_driver,name='delete_add_driver'),
    path('add_user1',views.add_user1,name='add_user1'),
    path('edit_add_user/<int:id>',views.edit_add_user,name='edit_add_user'),
    path('update_add_user/<int:id>',views.update_add_user,name='update_add_user'),
    path('delete_add_user/<int:id>',views.delete_add_user,name='delete_add_user'),
    path('add_customer1',views.add_customer1,name='add_customer1'),
    path('edit_add_customer/<int:id>',views.edit_add_customer,name='edit_add_customer'),
    path('update_add_customer/<int:id>',views.update_add_customer,name='update_add_customer'),
    path('delete_add_customer/<int:id>',views.delete_add_customer,name='delete_add_customer'),
    path('add_manage_income1',views.add_manage_income1,name='add_manage_income1'),
    path('edit_manage_income/<int:id>',views.edit_manage_income,name='edit_manage_income'),
    path('update_manage_income/<int:id>',views.update_manage_income,name='update_manage_income'),
    path('delete_manage_income/<int:id>',views.delete_manage_income,name='delete_manage_income'),
    path('add_manage_expense1',views.add_manage_expense1,name='add_manage_expense1'),
    path('edit_manage_expense/<int:id>',views.edit_manage_expense,name='edit_manage_expense'),
    path('update_manage_expense/<int:id>',views.update_manage_expense,name='update_manage_expense'),
    path('delete_manage_expense/<int:id>',views.delete_manage_expense,name='delete_manage_expense'),
    path('add_new_booking1',views.add_new_booking1,name='add_new_booking1'),
    path('edit_manage_booking/<int:id>',views.edit_manage_booking,name='edit_manage_booking'),
    path('update_manage_booking/<int:id>',views.update_manage_booking,name='update_manage_booking'),
    path('delete_manage_booking/<int:id>',views.delete_manage_booking,name='delete_manage_booking'),
    path('add_booking_quotation1',views.add_booking_quotation1,name='add_booking_quotation1'),
    path('edit_manage_booking_quotation/<int:id>',views.edit_manage_booking_quotation,name='edit_manage_booking_quotation'),
    path('update_manage_booking_quotation/<int:id>',views.update_manage_booking_quotation,name='update_manage_booking_quotation'),
    path('delete_manage_booking_quotation/<int:id>',views.delete_manage_booking_quotation,name='delete_manage_booking_quotation'),
    path('add_vendor1',views.add_vendor1,name='add_vendor1'),
    path('edit_add_vendor/<int:id>',views.edit_add_vendor,name='edit_add_user'),
    path('update_add_vendor/<int:id>',views.update_add_vendor,name='update_add_vendor'),
    path('delete_add_vendor/<int:id>',views.delete_add_vendor,name='delete_add_vendor'),
    path('add_fuel1',views.add_fuel1,name='add-fuel1'),
    path('edit_add_fuel/<int:id>',views.edit_add_fuel,name='edit_add_fuel'),
    path('update_add_fuel/<int:id>',views.update_add_fuel,name='update_add_fuel'),
    path('delete_add_fuel/<int:id>',views.delete_add_fuel,name='delete_add_fuel'),
    path('edit_profile_user',views.edit_profile_user,name='edit_profile_user'),
    path('edit_password_user',views.edit_password_user,name='edit_password_user'),
    path('add_vehicle_group',views.add_vehicle_group,name='add_vehicle_group'),
    path('note',views.note,name='note'),
    path('index_note',views.index_note,name='index_note'),




    path('reg_add_vehicle_type',views.reg_add_vehicle_type,name='reg_add_vehicle_type'),
    path('edit_vehicle_type/<int:id>',views.edit_vehicle_type,name='edit_vehicle_type'),
    path('edit_vehicle_type_update/<int:id>',views.edit_vehicle_type_update,name='edit_vehicle_type_update'),
    path('edit_vehicle_type_delete/<int:id>',views.edit_vehicle_type_delete,name='edit_vehicle_type_delete'),

    path('edit_vehicle_group/<int:id>',views.edit_vehicle_group,name='edit_vehicle_group'),
    path('edit_vehicle_group_update/<int:id>',views.edit_vehicle_group_update,name='edit_vehicle_group_update'),
    path('edit_vehicle_group_delete/<int:id>',views.edit_vehicle_group_delete,name='edit_vehicle_group_delete'),
    path('reg_add_vehicle_group',views.reg_add_vehicle_group,name='reg_add_vehicle_group'),
       

    path('reg_add_vehicle_inspection',views.reg_add_vehicle_inspection,name='reg_add_vehicle_inspection'),
    path('edit_vehicle_inspection/<int:id>',views.edit_vehicle_inspection,name='edit_vehicle_inspection'),
    path('edit_vehicle_inspection_update/<int:id>',views.edit_vehicle_inspection_update,name='edit_vehicle_inspection_update'),
    path('edit_vehicle_inspection_delete/<int:id>',views.edit_vehicle_inspection_delete,name='edit_vehicle_inspection_delete'),
    


    path('reg_add_manage_vehicle',views.reg_add_manage_vehicle,name='reg_add_manage_vehicle'), 
    path('edit_manage_vehicle/<int:id>',views.edit_manage_vehicle,name='edit_manage_vehicle'),
    path('edit_manage_vehicle_update/<int:id>',views.edit_manage_vehicle_update,name='edit_manage_vehicle_update'),
    path('edit_manage_vehicle_delete/<int:id>',views.edit_manage_vehicle_delete,name='edit_manage_vehicle_delete'),
 
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
