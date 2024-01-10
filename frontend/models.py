from django.db import models

# Create your models here



class registerdb(models.Model):
    # Name=models.CharField(max_length=20,null=True,blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=20,null=True,blank=True)
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)

class contactdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    subject=models.CharField(max_length=20,null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)

class spadb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    checkin=models.DateField(null=True,blank=True)
    checkout=models.DateField(null=True,blank=True)
    rooms=models.IntegerField(null=True,blank=True)
    adults=models.IntegerField(null=True,blank=True)
    children=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="id_image",null=True,blank=True)

class hotelbookdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    checkin=models.DateField(null=True,blank=True)
    checkout=models.DateField(null=True,blank=True)
    image=models.ImageField(upload_to="idimage2",null=True,blank=True)
    room=models.IntegerField(null=True,blank=True)
    adult=models.IntegerField(null=True,blank=True)
    children=models.IntegerField(null=True,blank=True)

class flightdb(models.Model):
    flyfrom=models.CharField(max_length=100,null=True,blank=True)
    flyto=models.CharField(max_length=100,null=True,blank=True)
    departing=models.DateField(null=True,blank=True)
    returning=models.DateField(null=True,blank=True)
    adult=models.IntegerField(null=True,blank=True)
    children=models.IntegerField(null=True,blank=True)
    travel=models.CharField(max_length=100,null=True,blank=True)

class booking_detailsdb(models.Model):
    activityname=models.CharField(max_length=100,null=True,blank=True)
    activityprice=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)



class booking_details_hoteldb(models.Model):
    hotelname = models.CharField(max_length=100, null=True, blank=True)
    hotelprice = models.IntegerField(null=True, blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)

class booking_details_spadb(models.Model):
    spaname = models.CharField(max_length=100, null=True, blank=True)
    spaprice = models.IntegerField(null=True, blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)

class paymentdb(models.Model):
    cardnumber=models.IntegerField(null=True,blank=True)
    monthyear=models.DateField(null=True,blank=True)
    cvv=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

class verify(models.Model):
    otp1=models.IntegerField(null=True,blank=True,)











