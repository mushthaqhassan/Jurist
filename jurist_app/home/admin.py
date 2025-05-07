from django.contrib import admin
from .models import Departments, Lawyers, Booking, Registration
from .models import ContactMessage, Advocate
# Register your models here.

admin.site.register(Departments)
admin.site.register(Lawyers)
admin.site.register(ContactMessage)
admin.site.register(Advocate)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','c_name','c_phone','c_email','law_name','dep_name','c_address','c_state','C_city','booking_date','booked_on')

admin.site.register(Booking, BookingAdmin)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id','l_name','l_phone','l_email','l_location','dep_name','l_education','l_address','law_exp')

admin.site.register(Registration, RegistrationAdmin)