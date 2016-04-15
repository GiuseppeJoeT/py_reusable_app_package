from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', register, name='login'),
    url(r'^logout/$', register, name='logout'),
    url(r'^profile/$', register, name='profile'),
]
