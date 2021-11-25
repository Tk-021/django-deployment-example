from django.conf.urls import url
from . import views

#TEMPLATE URLS!

app_name = 'basicapp'

urlpatterns=[
    url('register/$', views.register, name='register'),
]
