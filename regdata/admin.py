from django.contrib import admin

from regdata.models import insertdata
from regdata.models import passoutdata
from regdata.models import feedata
from regdata.models import feedata2

class insertdataadmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','phone_no','add','city','gender','course','btime','photo','fee','remfee')
    
admin.site.register(insertdata,insertdataadmin)



class passoutdataadmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','phone_no','add','city','gender','course','btime','photo','fee','remfee')
    
admin.site.register(passoutdata,passoutdataadmin)


class feedataadmin(admin.ModelAdmin):
    list_display=('regno','remfee','totalfee','fee','date')

admin.site.register(feedata,feedataadmin)

class feedata2admin(admin.ModelAdmin):
    list_display=('regno','remfee','totalfee','fee','todate')

admin.site.register(feedata2,feedata2admin)