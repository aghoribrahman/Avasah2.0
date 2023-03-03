from django.db import models



class Query_model(models.Model):  
    full_name = models.CharField(max_length=50)  
    phone_number  = models.CharField(max_length=12)
    email_id = models.EmailField()
    property_type = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    budget = models.IntegerField()
    other_info = models.TextField(max_length=300,default='None')

class Contact_model(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=13)
    email_id = models.EmailField()
    other_info = models.TextField(max_length=300,default='None')