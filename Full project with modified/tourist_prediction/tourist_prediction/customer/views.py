import subprocess

from django.db.models import Q, Count
from django.shortcuts import render, redirect

# Create your views here.
from admins.models import Uploadtourist
from customer.models import UserRegistration, Prediction, booking, Feeback_Model


def registerform(request):
    if request.method=="POST":
        userid = request.POST.get('userid')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobilenumber = request.POST.get('mobilenumber')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        UserRegistration.objects.create(userid=userid, firstname=firstname,lastname=lastname, email=email, password=password,mobilenumber=mobilenumber, dob=dob, gender=gender, address=address)
        return redirect('loginform')
    return render(request,'customer/registerform.html')


def loginform(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            check = UserRegistration.objects.get(email=email, password=password)
            request.session['userid'] = check.id
            return redirect('mydetails')
        except:
            pass
    return render(request,'customer/loginform.html')


def mydetails(request):
    userid = request.session['userid']
    ted = UserRegistration.objects.get(id=userid)
    return render(request,'customer/mydetails.html', {'object': ted})


def viewtou(request):
    obj=Uploadtourist.objects.all()
    return render(request,'customer/viewtou.html',{'objects':obj})

def search_touristplace(request):
    objw = ''
    if request.method == "POST":
        usid = request.POST.get('search')
        objw = Uploadtourist.objects.filter(Q(touplace=usid) | Q(neartou=usid))

        Prediction.objects.create(place=usid)

    return render(request,'customer/search_touristplace.html', {'objes': objw})


def view_prediction(request,pk):
    name = request.session['userid']
    userObj = UserRegistration.objects.get(id=name)
    gymObj = Uploadtourist.objects.get(id=pk)
    chart = Uploadtourist.objects.values('lat').annotate(dcount=Count('lat'))
    return render(request, 'customer/view_prediction.html', {'objects': gymObj,'form':chart})




def graph(request,grpchart_type):
    chart = Prediction.objects.values('place').annotate(dcount=Count('place')).order_by('-dcount')
    return render(request,"customer/graph.html", {'form':chart, 'chart_type':grpchart_type})


def bking(request,pp):
    name = request.session['userid']
    userObj = UserRegistration.objects.get(id=name)
    gymObj = Uploadtourist.objects.get(id=pp)



    if request.method=="POST":

        user = request.POST.get('username')
        pla = request.POST.get('touristpla')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        dayno = request.POST.get('dayno')

        booking.objects.create(uid=userObj, uploadid=gymObj,username=user, touristpla=pla, startdate=startdate,enddate=enddate, dayno=dayno)



    return render(request, 'customer/bking.html',{'form':userObj,'obj':gymObj})



def feedback(request):

    name = request.session['userid']
    Opj = UserRegistration.objects.get(id=name)
    if request.method == "POST":
        name = request.POST.get('name')

        feedback = request.POST.get('feedback')
        stars1 = request.POST.get('stars1')





        Feeback_Model.objects.create(name=Opj, cusname=name, feedback=feedback,stars1=stars1)

    return render(request, 'customer/feedback.html',{'form':Opj})


def quiz(requset):


    subprocess.run('python D:/tourist_prediction/quiz.py')


    return render(requset,'customer/quiz.html')




