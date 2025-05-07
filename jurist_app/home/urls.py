from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('lawyers', views.lawyers, name='lawyers'),
    path('contact', views.contact, name='contact'),
    path('creator', views.creator, name='creator'),
    path('appointment', views.appointment, name='appointment'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginn, name='login'),
    path('registerlawyer', views.registerlawyer, name='registerlawyer'),
    path('lawlogin', views.lawlogin, name='lawlogin'),
    path('lawsignup', views.lawsignup, name='lawsignup'),
    path('logout', views.logout, name='logout'),
    path('Findcase', views.Findcase, name='Findcase'),

]