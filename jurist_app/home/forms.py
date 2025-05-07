from django import forms


from .models import Booking
from .models import Registration

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
            
            
        }

        labels = {
           'c_name':' Name',
           'c_phone':'Phone Number',
           'c_email':'Email',
           'dep_name':'Department Name',
           'law_name':'Lawyer Name',
            'c_address':'Address',
           'booking_date':'Booking Date',
           'c_state':'State',
           'C_city':'City',

        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    
        widgets = {
        }

        labels = {
           'l_name':'Advocate Name',
           'l_phone':'Phone Number',
           'l_email':'Email',
           'dep_name':'Department Name',
           'l_location':'Location',
            'l_address':'Address',
           'law_exp':'Experience',
           'l_education':'Education',

        }