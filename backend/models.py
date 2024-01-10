from django.db import models

# Create your models here.
class placedb(models.Model):
    placename=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to="image",null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    # video_file = models.FileField(upload_to='videos')
    # description=models.CharField(max_length=20,null=True,blank=True)

class activitydb(models.Model):
    activity=models.CharField(max_length=20,null=True,blank=True)
    hour=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    activityimage=models.ImageField(upload_to="activityimage",null=True,blank=True)

class roomdb(models.Model):
    hotelname=models.CharField(max_length=20,null=True,blank=True)
    nights=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    # food=models.CharField(max_length=20,null=True,blank=True)
    Image=models.ImageField(upload_to="roomimage",null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    # roomimage=models.ImageField(upload_to="roomsimage",null=True,blank=True)
    image1=models.ImageField(upload_to="roomimage1",null=True,blank=True)
    image2=models.ImageField(upload_to="roomimage2",null=True,blank=True)
    image3=models.ImageField(upload_to="roomimage3",null=True,blank=True)



class resortdb(models.Model):
    ResortName=models.CharField(max_length=20,null=True,blank=True)
    Hour=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="resortimage",null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)


