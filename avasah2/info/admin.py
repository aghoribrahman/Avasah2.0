from django.contrib import admin
from .models import Query_model, Contact_model

@admin.register(Query_model)
class Query_model_admin(admin.ModelAdmin):
    list_display =["full_name","phone_number","email_id","property_type","area","budget","other_info"]

@admin.register(Contact_model)
class Contact_model_admin(admin.ModelAdmin):
    list_display =["full_name","phone_number","email_id",]