from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='Index'),
    url(r'^About/',views.about,name='About'),
    url(r'^Subscribe/',views.Subscribe,name='Subscribe'),
    url(r'^Notes/',views.notes,name='Notes'),
    url(r'^Search/',views.search,name='Search'),
    url(r'^AdminLogin/',views.adminlogin,name='AdminLogin'),
    url(r'^CheckLogin/',views.checklogin,name='CheckLogin'),
    url(r'^Upload/',views.upload,name='Upload'),
]
