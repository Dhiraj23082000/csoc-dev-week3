from django.urls import path
from store.views import *


urlpatterns = [
    path('',index,name="index"),

    path('^login/$',loginiew, name = "login"),

    path('^logout/$',logoutView, name = "logout"),

]
