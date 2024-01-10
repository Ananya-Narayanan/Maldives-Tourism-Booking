from django.shortcuts import render,redirect
from backend.models import placedb,activitydb,roomdb,resortdb
from frontend.models import contactdb,spadb,hotelbookdb,paymentdb,booking_detailsdb,booking_details_hoteldb,booking_details_spadb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse

# Create your views here.
def indexpg(request):
    return render(request,"index.html")

def addplace(request):
    return render(request,"add places.html")

def save_place(request):
    if request.method=="POST":
        p=request.POST.get('pname')
        ci=request.POST.get('city')
        # d=request.POST.get('desc')
        im=request.FILES['img']
        # v=request.POST.get['vedio']
        obj=placedb(placename=p,city=ci,image=im)
        obj.save()
        messages.success(request, "Place saved successfully")
        return redirect(addplace)

def display_place(request):
    data=placedb.objects.all()
    return render(request,"display places.html",{'data':data})

def edit_place(request,dataid):
    editpl=placedb.objects.get(id=dataid)
    return render(request,"edit.html",{'editpl':editpl})

def update_place(request,dataid):
    if request.method=="POST":
        p = request.POST.get('pname')
        ci = request.POST.get('city')
        # d = request.POST.get('desc')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=placedb.objects.get(id=dataid).image
        placedb.objects.filter(id=dataid).update(placename=p,city=ci,image=file)
        messages.success(request, "updated  successfully")
        return redirect(display_place)

def delete_place(request,dataid):
    dele=placedb.objects.filter(id=dataid)
    dele.delete()
    messages.warning(request, "Place deleted successfully")
    return redirect(display_place)

def activities(request):
    return render(request,"activities.html")

def save_activity(request):
    if request.method=="POST":
        ac=request.POST.get('act')
        h=request.POST.get('hour')
        p=request.POST.get('price')
        im=request.FILES['img']
        obj=activitydb(activity=ac,hour=h,price=p,activityimage=im)
        obj.save()
        messages.success(request, "Activity saved successfully")
        return redirect(activities)


def displayactivity(request):
    data_activity=activitydb.objects.all()
    return render(request,"display_activity.html",{'data_activity':data_activity})

def editactivity(request,dataid):
    editact=activitydb.objects.get(id=dataid)
    return render(request,"edit_activity.html",{'editact':editact})

def update_activity(request,dataid):
    if request.method == "POST":
        ac = request.POST.get('act')
        h = request.POST.get('hour')
        p = request.POST.get('price')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = activitydb.objects.get(id=dataid).activityimage
        activitydb.objects.filter(id=dataid).update(activity=ac,hour=h,price=p,activityimage=file)
        messages.success(request, "updated  successfully")
        return redirect(displayactivity)

def delete_activity(request,dataid):
    dele = activitydb.objects.filter(id=dataid)
    dele.delete()
    messages.warning(request, "Activity deleted successfully")
    return redirect(displayactivity)

def addhotels(request):
    return render(request,"add_hotels.html")


def save_room(request):
    if request.method == "POST":
        try:
            hn = request.POST.get('hname')
            n = request.POST.get('night')
            p = request.POST.get('price')
            im = request.FILES['imge']
            l = request.POST.get('location')
            d = request.POST.get('desc')
            img1 = request.FILES['rimg1']
            img2 = request.FILES['rimg2']
            img3 = request.FILES['rimg3']

            obj = roomdb(hotelname=hn, nights=n, price=p, Image=im, location=l, description=d, image1=img1, image2=img2,
                         image3=img3)
            obj.save()
            messages.success(request, "Hotel saved successfully")
            return redirect(addhotels)

        except KeyError as e:
            messages.error(request, f"Error: {e}. Some required fields/files are missing.")
            return redirect(addhotels)  # Redirect to an appropriate page or handle the error accordingly


def display_hotels(request):
    datahotel=roomdb.objects.all()
    return render(request,"display_hotels.html",{'datahotel':datahotel})

def edit_hotel(request,dataid):
    edithotel=roomdb.objects.get(id=dataid)
    return render(request,"edit_hotel.html",{'edithotel':edithotel})

def update_hotel(request, dataid):
    if request.method == "POST":
        hn = request.POST.get('hname')
        n = request.POST.get('night')
        p = request.POST.get('price')
        l = request.POST.get('location')
        d = request.POST.get('desc')

        try:
            im = request.FILES['imge']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file=roomdb.objects.get(id=dataid).Image

        try:
            img1 = request.FILES['rimg1']
            fs=FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1=roomdb.objects.get(id=dataid).image1

        try:
            img2 = request.FILES['rimg2']
            fs=FileSystemStorage()
            file2=fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2=roomdb.objects.get(id=dataid).image2

        try:
            img3 = request.FILES['rimg3']
            fs=FileSystemStorage()
            file3=fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3=roomdb.objects.get(id=dataid).image3

        roomdb.objects.filter(id=dataid).update(
            hotelname=hn, nights=n, price=p, Image=file, location=l, description=d, image1=file1, image2=file2, image3=file3
        )
        messages.success(request, "Updated successfully")
        return redirect(display_hotels)


def delete_hotels(request,dataid):
    dele = roomdb.objects.filter(id=dataid)
    dele.delete()
    messages.warning(request, "Hotel deleted successfully")
    return redirect(display_hotels)

def add_spa(request):
    return render(request,"add_spa.html")

def save_spa(request):
    if request.method=="POST":
        rn=request.POST.get('rname')
        h=request.POST.get('hour')
        p=request.POST.get('price')
        im=request.FILES['img']
        l=request.POST.get('location')
        obj=resortdb(ResortName=rn,Hour=h,Price=p,image=im,location=l)
        obj.save()
        messages.success(request, "Spa Resorts saved successfully")
        return redirect(add_spa)

def display_spa(request):
    dataspa=resortdb.objects.all()
    return render(request,"display_spa.html",{'dataspa':dataspa})

def edit_spa(request,dataid):
    editspa=resortdb.objects.get(id=dataid)
    return render(request,"edit_spa.html",{'editspa':editspa})

def update_spa(request,dataid):
    if request.method=="POST":
        rn=request.POST.get('rname')
        h=request.POST.get('hour')
        p=request.POST.get('price')
        l = request.POST.get('location')
        try:
            im = request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=resortdb.objects.get(id=dataid).image
        resortdb.objects.filter(id=dataid).update(ResortName=rn,Hour=h,Price=p,image=file,location=l)
        messages.success(request, "updated  successfully")
        return redirect(display_spa)

def delete_spa(request,dataid):
    dele=resortdb.objects.filter(id=dataid)
    dele.delete()
    messages.warning(request, "Spa Resort deleted successfully")
    return redirect(display_spa)

def admin(request):
    return render(request,"adminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                # messages.success(request,"Logined successfully")
                return redirect(indexpg)

            else:
                messages.warning(request, "incorrect username/password")
                return redirect(admin)
        else:
            return redirect(admin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request, "Logout successfully")
    return redirect(admin)


def viewcontact(request):
    data=contactdb.objects.all()
    return render(request,"viewcontact.html",{'data':data})

def deletecontact(request,dataid):
    datadelete=contactdb.objects.filter(id=dataid)
    datadelete.delete()
    return redirect(viewcontact)

def view_spabooking(request):
    data=spadb.objects.all()
    return render(request,"view_spabooking.html",{'data':data})

def delete_spabooking(request,dataid):
    datadelete=spadb.objects.filter(id=dataid)
    datadelete.delete()
    return redirect(view_spabooking)

def view_hotelbooking(request):
    datas1=hotelbookdb.objects.filter(username=request.session['Username'])
    return render(request,"view_hotelbooking.html",{'datas1':datas1})

def delete_hotelbooking(request,dataid):
    datadelete=hotelbookdb.objects.filter(id=dataid)
    datadelete.delete()
    return redirect(view_hotelbooking)
def view_payment(request):
    data=paymentdb.objects.filter(username=request.session['Username'])
    return render(request,"view_payment.html",{'data':data})

def delete_payment(request,payid):
    deletepay=paymentdb.objects.filter(id=payid)
    deletepay.delete()
    return redirect(view_payment)

def view_booked_details_backend(request):
    data = booking_detailsdb.objects.filter(username=request.session['Username'])
    data1 = booking_details_hoteldb.objects.filter(username=request.session['Username'])
    data2 = booking_details_spadb.objects.filter(username=request.session['Username'])

    total_activity_price = data.aggregate(total_activity_price=Sum('activityprice'))['total_activity_price']
    total_hotel_price = data1.aggregate(total_hotel_price=Sum('hotelprice'))['total_hotel_price']
    total_spa_price = data2.aggregate(total_spa_price=Sum('spaprice'))['total_spa_price']

    total_price = sum(filter(None, [total_activity_price, total_hotel_price, total_spa_price]))
    return render(request,"booked_details_backend.html",{
        'data': data,
        'data1': data1,
        'data2': data2,
        'total_price': total_price
    })









