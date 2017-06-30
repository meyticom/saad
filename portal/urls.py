from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from portal import views

urlpatterns = [
    url(r'^et/(?P<pk>\d+)/$', views.teacher_edit, name='teacher_edit'),
    url(r'^teacher', views.teacherview, name='teacherview'),
    url(r'^add_student', views.add_student, name='add_student'),
    url(r'^financial', views.financial, name='financial'),
    url(r'^$', views.add_student, name='add_student'),
    url(r'^all', views.all_student, name='all_student'),
    url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





