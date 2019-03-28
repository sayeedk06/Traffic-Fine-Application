from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

# This contains the url patterns that will be used by user
# to move from one page to another

urlpatterns = [
    path('assignFine/',views.fine,name='assignFine')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
