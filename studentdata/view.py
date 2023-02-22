from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from regdata.models import insertdata
from regdata.models import passoutdata
from regdata.models import feedata, feedata2 
from datetime import date





def home(request):
    return render(request,"home.html")

def reg(request):
    try:
        if request.method=="POST":
            regno="ducat"
            name=request.POST.get('name')
            fname=request.POST.get('fname')
            mname=request.POST.get('mname')
            phone_no=request.POST.get('phoneno')
            add=request.POST.get('address')
            city=request.POST.get('city')
            gender=request.POST.get('gender')
            course=request.POST.get('course')
            btime=request.POST.get('btime')
            photo=request.FILES['photo']
            fee=request.POST.get('fee')
            remfee=request.POST.get('fee')
            data=insertdata(regno=regno,name=name,fname=fname,mname=mname,phone_no=phone_no,add=add,city=city,gender=gender,course=course,btime=btime,photo=photo,fee=fee,remfee=remfee)
            data.save()
            data=insertdata.objects.all().order_by('-id')[0]
            fid=data.id
            regno="ducat"+str(fid)
            data=insertdata(id=fid,regno=regno,name=name,fname=fname,mname=mname,phone_no=phone_no,add=add,city=city,gender=gender,course=course,btime=btime,photo=photo,fee=fee,remfee=remfee)
            data.save()

    except:
        pass
    return render(request,"registration.html")

def viewdata(request):
    return render(request,"view.html")
def viewall(request):
    data=insertdata.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"viewall.html",data1)
def viewbybtime(request):
    try:
        if  request.method=="POST":
            fbtime=request.POST.get('btime')
            url="/fviewbybtime/"+fbtime
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbybatchtime.html")


def fviewbybtime(request,btime):
    b_time=insertdata.objects.filter(btime=btime)
    data={
        'batchtime':b_time
    }
    return render(request,"viewbybatchtime1.html",data)
def viewbyregno(request):
    try:
        if request.method=="POST":
            fregno=request.POST.get('regno')
            url="/fviewbyregno/"+fregno
            return HttpResponseRedirect(url)
    except:
        pass
    return render (request,"viewbyregno.html")

def fviewbyregno(request,regno):
    f_regno=insertdata.objects.get(regno=regno)
    data1={
        're':f_regno
    }
    return render (request,"viewbyregno1.html",data1)

def viewbyname(request):
    try:
        if request.method=="POST":
            fname=request.POST.get('name')
            url="/fviewbyname/"+fname
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbyname.html")
def fviewbyname(request,uname):
    f_name=insertdata.objects.filter(name=uname)
    data={
        'namedata':f_name
    }
    return render(request,"viewbyname1.html",data)
def delete(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            fregno=insertdata.objects.get(regno=regno)
            tregno=fregno.regno
            name=fregno.name
            fname=fregno.fname
            mname=fregno.mname
            phone_no=fregno.phone_no
            add=fregno.add
            city=fregno.city
            gender=fregno.gender
            course=fregno.course
            btime=fregno.btime
            photo=fregno.photo
            fee=fregno.fee
            remfee=fregno.remfee
            data=passoutdata(regno=tregno,name=name,fname=fname,mname=mname,phone_no=phone_no,add=add,city=city,gender=gender,course=course,btime=btime,photo=photo,fee=fee,remfee=remfee)
            data.save()
            fregno.delete()

            url="/delete/"
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"delete.html")

def update(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            url="/fupdate/"+regno
            return HttpResponseRedirect(url)
    except:
        pass

    return render(request,"update.html")
def fupdate(request,update):
    f_regno=insertdata.objects.get(regno=update)
    uid=f_regno.id
    data={
        'freg':f_regno
    }
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            fname=request.POST.get('fname')
            mname=request.POST.get('mname')
            phone_no=request.POST.get('phoneno')
            add=request.POST.get('add')
            city=request.POST.get('city')
            gender=request.POST.get('gender')
            course=request.POST.get('course')
            btime=request.POST.get('btime')
            photo=request.POST.get('photo')
            fee=request.POST.get('fee')
            data1=insertdata(
                id=uid,
                regno=update,
                name=name,
                fname=fname,
                mname=mname,
                phone_no=phone_no,
                add=add,
                city=city,
                gender=gender,
                course=course,
                btime=btime,
                photo=photo,
                fee=fee,
            
                )
            data1.save()

    
    except:
        pass
    return render(request,"update1.html",data)


def fee(request):
    return render(request,"fee.html")
def subfee(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            url="/subfee1/"+regno
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"submitfee.html")

def subfee1(request,fregno):
    fregno=insertdata.objects.get(regno=fregno)
    data={
        "feedata":fregno
    }
    try:
        if request.method=="POST":
            regno=fregno.regno
            fees=request.POST.get('fee')
            today1=date.today()
            totalfee=fregno.remfee
            rem=int(totalfee)-int(fees)
            subfee=feedata2(
                regno=regno,
                fee=fees,
                totalfee=totalfee,
                date=today1,
                rem=rem,
                )
            subfee.save()

            uid=fregno.id

            preet=insertdata(
                id=uid,
                regno=fregno.regno,
                name=fregno.name,
                fname=fregno.fname,
                mname=fregno.mname,
                phone_no=fregno.phone_no,
                add=fregno.add,
                city=fregno.city,
                gender=fregno.gender,
                course=fregno.course,
                btime=fregno.btime,
                photo=fregno.photo,
                fee=fregno.fee,
                remfee=rem,)
            preet.save()
    except:
        pass
    return render(request,"submitfee1.html",data)
    
def viewfee(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            url="/fviewfee/"+regno
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewfee.html")

def fviewfee(request,fregno):
    tregno=insertdata.objects.get(regno=fregno)
    data1={
        'fee':tregno
    }
    return render(request,"viewfee1.html",data1)
def passout(request):
    data=passoutdata.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"passedoutstudent.html",data1)
