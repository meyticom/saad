from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from student import views

urlpatterns = [


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





