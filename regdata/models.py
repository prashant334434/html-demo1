from django.db import models
from distutils.command.upload import upload

class insertdata(models.Model):
    regno=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    fname=models.CharField( max_length=50)
    mname=models.CharField( max_length=50)
    phone_no=models.CharField( max_length=50)
    add=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    course=models.CharField( max_length=50)
    btime=models.CharField( max_length=50)
    photo=models.ImageField(upload_to='static/studentimage',default="")
    fee=models.CharField( max_length=50)
    remfee=models.CharField( max_length=50)


class passoutdata(models.Model):
    regno=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    fname=models.CharField( max_length=50)
    mname=models.CharField( max_length=50)
    phone_no=models.CharField( max_length=50)
    add=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    course=models.CharField( max_length=50)
    btime=models.CharField( max_length=50)
    photo=models.CharField( max_length=50)
    fee=models.CharField( max_length=50)
    remfee=models.CharField( max_length=50)


class feedata(models.Model):
    regno=models.CharField(max_length=50)
    remfee=models.CharField(max_length=50)
    totalfee=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

class feedata2(models.Model):
    regno=models.CharField(max_length=50)
    remfee=models.CharField(max_length=50)
    totalfee=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    todate=models.CharField(max_length=50)
