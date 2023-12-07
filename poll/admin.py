from django.contrib import admin
from  .models import Userinfo



class UserinfoAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","phone","date",)

# Register your models here.
admin.site.register(Userinfo,UserinfoAdmin)