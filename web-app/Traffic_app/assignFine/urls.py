from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views


# This contains the url patterns that will be used by user
# to move from one page to another

urlpatterns = [
    path('assignFine/',views.Fine,name='assignFine')

]
