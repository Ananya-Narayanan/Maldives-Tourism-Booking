from django.urls import path
from frontend import views

urlpatterns=[
    path('homepg/',views.homepg,name="homepg"),
    path('destination/<int:hotelid>/',views.destination,name="destination"),
    path('singlespa/<int:spaid>/',views.singlespa,name="singlespa"),
    path('singleactivity/<int:actid>/',views.singleactivity,name="singleactivity"),
    path('spabooking/',views.spabooking,name="spabooking"),
    path('savespa/',views.savespa,name="savespa"),
    path('about/',views.about,name="about"),
    path('',views.register,name="register"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('hotelbooking/', views.hotelbooking, name="hotelbooking"),
    path('savehotelbooking/', views.savehotelbooking, name="savehotelbooking"),
    path('booked_detail/',views.booked_detail,name="booked_detail"),
    path('save_bookeddetail/',views.save_bookeddetail,name="save_bookeddetail"),
    path('save_bookeddetails_hotel/',views.save_bookeddetails_hotel,name="save_bookeddetails_hotel"),
    path('save_bookeddetails_spa/',views.save_bookeddetails_spa,name="save_bookeddetails_spa"),
    path('delete_booking/<int:dataid>/',views.delete_booking,name="delete_booking"),
    path('delete_booking_hotel/<int:hotelid>/',views.delete_booking_hotel,name="delete_booking_hotel"),
    path('delete_booking_spa/<int:spaid>/',views.delete_booking_spa,name="delete_booking_spa"),
    path('paymentpage/',views.paymentpage,name="paymentpage"),
    path('savepayment/',views.savepayment,name="savepayment"),
    path('otpfetch/',views.otpfetch,name="otpfetch"),
    path('saveotp/',views.saveotp,name="saveotp"),
    path('generate_invoice/',views.generate_invoice,name="generate_invoice"),








]