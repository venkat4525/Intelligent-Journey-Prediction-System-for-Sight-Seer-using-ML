from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from admins.models import Uploadtourist
from customer.models import UserRegistration, Feeback_Model, booking


def admin_loginpage(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('view_user_details')
    return render(request,'admins/admin_loginpage.html')

def view_user_details(request):
    obj=UserRegistration.objects.all()
    return render(request,'admins/view_user_details.html',{'obje':obj})


def upload_tourist(request, x_train=None, y_train=None):

    if request.method == "POST" and request.FILES['touimg']:
        touplace =request.POST.get('touplace')
        neartou = request.POST.get('neartou')
        spc = request.POST.get('spc')
        touimg = request.FILES['touimg']
        touimg1 = request.FILES['touimg1']

        log = request.POST.get('log')
        lat = request.POST.get('lat')


        Uploadtourist.objects.create(touplace=touplace, neartou=neartou, spc=spc, touimg=touimg,touimg1=touimg1,
                                   log=log,lat=lat)

    return render(request, 'admins/upload_tourist.html')



def view_tourist(request):
    ted = Uploadtourist.objects.all()

    return render(request, 'admins/view_tourist.html',{'objects':ted})

def cusbooking(request):
    ted = booking.objects.all()

    return render(request, 'admins/cusbooking.html',{'objects':ted})

def view_feedback(request):
    ted = Feeback_Model.objects.all()

    return render(request, 'admins/view_feedback.html',{'objects':ted})

def tourist(request,chart_type):
    chart = Uploadtourist.objects.values('touplace').annotate(dcount=Count('touplace')).order_by('-dcount')
    return render(request,"admins/tourist.html", {'form':chart, 'chart_type':chart_type})



















