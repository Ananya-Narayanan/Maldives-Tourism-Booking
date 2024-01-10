
from backend.models import placedb,activitydb,roomdb,resortdb
from frontend.models import registerdb,contactdb,spadb,hotelbookdb,booking_detailsdb,booking_details_hoteldb,booking_details_spadb,paymentdb,verify
from django.shortcuts import render
from django.db.models import Sum
from django.shortcuts import redirect
from django.contrib import messages


from django.http import HttpResponse
from fpdf import FPDF
import os
from django.http import HttpRequest

from django.contrib.auth.decorators import login_required




# Create your views here.
def homepg(request):
    data = placedb.objects.all()
    data_activity=activitydb.objects.all()
    data_hotel=roomdb.objects.all()
    data_spa=resortdb.objects.all()
    return render(request,"home.html",{'data':data,'data_activity':data_activity,'data_hotel':data_hotel,'data_spa':data_spa})

def destination(request,hotelid):
    data_hotel = roomdb.objects.get(id=hotelid)
    return render(request,"single_hotel.html",{'data_hotel':data_hotel})

def singlespa(request,spaid):
    data_spa=resortdb.objects.get(id=spaid)
    return render(request,"single_spa.html",{'data_spa':data_spa})

def singleactivity(request,actid):
    data_activity=activitydb.objects.get(id=actid)
    return render(request,"single_activity.html",{'data_activity':data_activity})

def spabooking(request):
    datas = spadb.objects.filter(username=request.session['Username'])
    return render(request, "spa_booking.html", {'datas': datas})

def about(request):
    return render(request,"about.html")

def register(request):
    return render(request,"register.html")

def saveregister(req):
    if req.method=="POST":

        m = req.POST.get('mob')
        e=req.POST.get('email')
        u = req.POST.get('user')
        p=req.POST.get('pass')
        obj=registerdb(Mobile=m,Email=e,Username=u,Password=p)
        obj.save()
        return redirect(register)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if registerdb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request,"Logined successfully")
            return redirect(homepg)
        else:
            messages.warning(request, "incorrect username/passwword")
            return redirect(register)
    return redirect(register)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.warning(request, "Logout successfully")
    return redirect(userlogin)

def contact(request):
    return render(request,"contact.html")

def savecontact(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        s=request.POST.get('sub')
        m=request.POST.get('message')
        obj=contactdb(name=n,email=e,subject=s,message=m)
        obj.save()
        return redirect(contact)


def hotelbooking(request):
    data=hotelbookdb.objects.filter(username=request.session['Username'])
    return render(request,"hotel_booking.html",{'data':data})

def savespa(request):
    if request.method=="POST":
        user = request.POST.get('User')
        n = request.POST.get('name')
        cin = request.POST.get('checkin')
        cout = request.POST.get('checkout')
        r = request.POST.get('rooms')
        a = request.POST.get('adult')
        c = request.POST.get('children')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        im = request.FILES['imgs']
        obj = spadb(username=user, name=n, checkin=cin, checkout=cout, rooms=r, adults=a, children=c, email=e,
                    phone=p, image=im)
        obj.save()
        messages.success(request, "Booked Successfully")
        return redirect(spabooking)





def savehotelbooking(request):
    if request.method=="POST":
        user=request.POST.get('User')
        n=request.POST.get('name')
        chin=request.POST.get('checkin')
        chout=request.POST.get('checkout')
        im=request.FILES['img']
        r=request.POST.get('room')
        a=request.POST.get('adult')
        c=request.POST.get('children')
        obj=hotelbookdb(username=user,name=n,checkin=chin,checkout=chout,image=im,room=r,adult=a,children=c)
        obj.save()
        messages.success(request, "Booked Successfully")
        return redirect(hotelbooking)

def booked_detail(request):
    data = booking_detailsdb.objects.filter(username=request.session['Username'])
    data1 = booking_details_hoteldb.objects.filter(username=request.session['Username'])
    data2 = booking_details_spadb.objects.filter(username=request.session['Username'])

    total_activity_price = data.aggregate(total_activity_price=Sum('activityprice'))['total_activity_price']
    total_hotel_price = data1.aggregate(total_hotel_price=Sum('hotelprice'))['total_hotel_price']
    total_spa_price = data2.aggregate(total_spa_price=Sum('spaprice'))['total_spa_price']

    total_price = sum(filter(None, [total_activity_price, total_hotel_price, total_spa_price]))

    return render(request, "Booked_details.html", {
        'data': data,
        'data1': data1,
        'data2': data2,
        'total_price': total_price
    })
def save_bookeddetail(request):
    if request.method=="POST":
        u=request.POST.get('user')
        actname=request.POST.get('activityname')
        actprice=request.POST.get('activityprice')
        obj=booking_detailsdb(activityname=actname,activityprice=actprice,username=u)
        obj.save()
        return redirect(booked_detail)

def save_bookeddetails_hotel(request):
    if request.method=="POST":
        us = request.POST.get('username')
        hname=request.POST.get('hotel')
        hprice=request.POST.get('price')
        obj=booking_details_hoteldb(hotelname=hname,hotelprice=hprice,username=us)
        obj.save()
        return redirect(booked_detail)

def save_bookeddetails_spa(request):
    if request.method=="POST":
        u = request.POST.get('user')
        spname=request.POST.get('spaname')
        sprice=request.POST.get('spaprice')
        obj=booking_details_spadb(spaname=spname,spaprice=sprice,username=u)
        obj.save()
        return redirect(booked_detail)

def delete_booking(request,dataid):
    dele=booking_detailsdb.objects.filter(id=dataid)
    dele.delete()
    return redirect(booked_detail)

def delete_booking_hotel(request,hotelid):
    delete_hotel=booking_details_hoteldb.objects.filter(id=hotelid)
    delete_hotel.delete()
    return redirect(booked_detail)

def delete_booking_spa(request,spaid):
    delete_spa=booking_details_spadb.objects.filter(id=spaid)
    delete_spa.delete()
    return redirect(booked_detail)

def paymentpage(request):
    data=paymentdb.objects.filter(username=request.session['Username'])
    return render(request,"payment.html",{'data':data})

def savepayment(request):
    if request.method=="POST":
        u=request.POST.get('User')
        cn=request.POST.get('cname')
        my=request.POST.get('monthyr')
        cvv=request.POST.get('cvv')
        n=request.POST.get('name')
        obj=paymentdb(username=u,cardnumber=cn,monthyear=my,cvv=cvv,name=n)
        obj.save()
        return redirect(otpfetch)

def otpfetch(request):
    return render(request,"otp_fetching.html")

def saveotp(request):
    if request.method=="POST":
        o1=request.POST.get('otp1')
        obj=verify(otp1=o1)
        obj.save()
        return redirect(generate_invoice)
        # messages.success(request, " Congratulations...!Payment successfull..!")




class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Invoice', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def calculate_total_price(request):
        data = booking_detailsdb.objects.filter(username=request.session['Username'])
        data1 = booking_details_hoteldb.objects.filter(username=request.session['Username'])
        data2 = booking_details_spadb.objects.filter(username=request.session['Username'])

        total_activity_price = data.aggregate(total_activity_price=Sum('activityprice'))['total_activity_price']
        total_hotel_price = data1.aggregate(total_hotel_price=Sum('hotelprice'))['total_hotel_price']
        total_spa_price = data2.aggregate(total_spa_price=Sum('spaprice'))['total_spa_price']

        total_price = sum(filter(None, [total_activity_price, total_hotel_price, total_spa_price]))


        # For example, summing up prices of items in an order
        return  total_price



def generate_invoice(request):
    pdf = PDF()
    pdf.add_page()

    if request.session.get('Username'):
        Username = request.session['Username']
    else:
        Username = "Anonymous"




    # Invoice Details
    pdf.set_font('Arial', '', 15)
    # pdf.cell(0, 10, 'Invoice Date: December 27, 2023', 0, 1)
    pdf.cell(0, 10, 'Invoice Number: INV-001', 0, 1)
    pdf.ln(10)

    # Payment Details
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(0, 10, 'Payment Details', 0, 1)
    pdf.ln(5)

    pdf.set_font('Arial', '', 15)
    pdf.cell(0, 10, f'Name: {Username}', 0, 1)
    # pdf.cell(0, 10, f'Amount:{total_price}', 0, 1)
    pdf.cell(0, 10, 'Payment Method: Credit Card', 0, 1)
    pdf.cell(0, 10, 'Transaction ID: ABC123XYZ', 0, 1)
    pdf.cell(0, 10, 'Payment successfully completed', 0, 1)


    # File path to save the generated PDF
    pdf_file_path = os.path.join(os.getcwd(), 'invoice.pdf')

    # Save the generated PDF to the specified file path
    pdf.output(pdf_file_path)

    # Provide the file as a download using Django's HttpResponse
    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response





















