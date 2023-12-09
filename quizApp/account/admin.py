from django.contrib import admin
from account.models import SignUpModel

# Register your models here.

@admin.register(SignUpModel)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["id" ,"username" , "email" , "gender" ]



