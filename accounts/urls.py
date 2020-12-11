from django.conf.urls import url
from .views import *
urlpatterns = [

    url(r'^register/$', account_register),
    url(r'^login/$', account_login)
]