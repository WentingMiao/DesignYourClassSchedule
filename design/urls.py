from django.conf.urls import url
from .views import *
urlpatterns = [

    url(r'^index/$', index),
    url(r'^demo/$', demo),
    url(r'^event/create/', event_create),
]