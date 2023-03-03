from django import forms
from .models import Query_model, Contact_model


class Query_form(forms.ModelForm):
    
    class Meta:
       
        model = Query_model 

        fields = "__all__"

        widgets = {
            'full_name' : forms.TextInput(attrs={'required': True ,'class' : 'form-control row w-50 p-3 mx-5 '}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'email_id' : forms.EmailInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'property_type' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'area' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'budget' : forms. NumberInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'other_info' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            }


class Contact_form(forms.ModelForm):
    
    class Meta:
       
        model = Contact_model 

        fields = "__all__"

        widgets = {
            'full_name' : forms.TextInput(attrs={'required': True ,'class' : 'form-control row w-50 p-3 mx-5 '}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'email_id' : forms.EmailInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            'other_info' : forms.TextInput(attrs={'class' : 'form-control row w-50 p-3 mx-5'}),
            }


