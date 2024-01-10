from django.urls import path
from backend import views

urlpatterns=[
    path('indexpg/',views.indexpg,name="indexpg"),
    path('addplace/',views.addplace,name="addplace"),
    path('save_place/',views.save_place,name="save_place"),
    path('display_place/',views.display_place,name="display_place"),
    path('edit_place/<int:dataid>/',views.edit_place,name="edit_place"),
    path('update_place/<int:dataid>/',views.update_place,name="update_place"),
    path('delete_place/<int:dataid>/',views.delete_place,name="delete_place"),
    path('activities/',views.activities,name="activities"),
    path('save_activity/',views.save_activity,name="save_activity"),
    path('displayactivity/',views.displayactivity,name="displayactivity"),
    path('editactivity/<int:dataid>/',views.editactivity,name="editactivity"),
    path('update_activity/<int:dataid>/',views.update_activity,name="update_activity"),
    path('delete_activity/<int:dataid>/',views.delete_activity,name="delete_activity"),
    path('addhotels/',views.addhotels,name="addhotels"),
    path('save_room/',views.save_room,name="save_room"),
    path('display_hotels/',views.display_hotels,name="display_hotels"),
    path('edit_hotel/<int:dataid>/',views.edit_hotel,name="edit_hotel"),
    path('update_hotel/<int:dataid>/',views.update_hotel,name="update_hotel"),
    path('delete_hotels/<int:dataid>/',views.delete_hotels,name="delete_hotels"),
    path('add_spa/',views.add_spa,name="add_spa"),
    path('save_spa/',views.save_spa,name="save_spa"),
    path('display_spa/',views.display_spa,name="display_spa"),
    path('edit_spa/<int:dataid>/',views.edit_spa,name="edit_spa"),
    path('update_spa/<int:dataid>/',views.update_spa,name="update_spa"),
    path('delete_spa/<int:dataid>/',views.delete_spa,name="delete_spa"),
    path('admin/',views.admin,name="admin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('viewcontact/',views.viewcontact,name="viewcontact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('view_spabooking/',views.view_spabooking,name="view_spabooking"),
    path('delete_spabooking/<int:dataid>/',views.delete_spabooking,name="delete_spabooking"),
    path('view_hotelbooking/',views.view_hotelbooking,name="view_hotelbooking"),
    path('delete_hotelbooking/<int:dataid>/',views.delete_hotelbooking,name="delete_hotelbooking"),
    path('view_payment/',views.view_payment,name="view_payment"),
    path('delete_payment/<int:payid>/',views.delete_payment,name="delete_payment"),
    path('view_booked_details_backend/',views.view_booked_details_backend,name="view_booked_details_backend")





]