from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from portal import views

urlpatterns = [

    url(r'^add_teacher', views.add_teacher, name='add_teacher'),
    url(r'^add_student', views.add_student, name='add_student'),
    url(r'^financial', views.financial, name='financial'),
    url(r'^$', views.add_student, name='add_student'),
    url(r'^all', views.all_student, name='all_student'),
    url(r'^post/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





