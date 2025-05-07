from django.db import models


# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()

    def __str__(self):
        return self.dep_name

class Lawyers(models.Model):
    law_name = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    law_exp = models.IntegerField()
    law_edu = models.TextField()
    law_image = models.ImageField(upload_to='lawyers')
    
    def __str__(self):
        return self.law_name

class Advocate(models.Model):
    law_name = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    law_exp = models.IntegerField()
    law_rating = models.CharField(max_length=255)
    law_location = models.CharField(max_length=255)
    case_lose = models.IntegerField()
    case_won = models.IntegerField()
    law_image = models.ImageField(upload_to='lawyers')

    def __str__(self):
        return self.law_name

class Booking(models.Model):
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    law_name = models.ForeignKey(Lawyers, on_delete=models.CASCADE)
    dep_name =  models.ForeignKey(Departments, on_delete=models.CASCADE)
    c_address = models.TextField()
    c_state = models.CharField(max_length=255)
    C_city = models.CharField(max_length=255)
    booking_date = models.DateField()
    booked_on = models.DateField (auto_now=True)

class Registration(models.Model):
    l_name = models.CharField(max_length=255)
    l_phone = models.CharField(max_length=10)
    l_email = models.EmailField()
    l_location = models.CharField(max_length=255)
    l_education = models.TextField()
    dep_name =  models.ForeignKey(Departments, on_delete=models.CASCADE)
    l_address = models.TextField()
    law_exp = models.IntegerField()

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name