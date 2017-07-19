from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from portal import views

urlpatterns = [
                  url(r'^edit_teacher/(?P<pk>\d+)/$', views.edit_teacher, name='edit_teacher'),
                  url(r'^teacher', views.teacherview, name='teacherview'),
                  url(r'^add_student', views.add_student, name='add_student'),
                  url(r'^add_teacher', views.add_teacher, name='add_teacher'),
                  url(r'^students', views.all_student, name='all_student'),
                  url(r'^student/(?P<pk>\d+)/$', views.student_edit, name='student_edit'),
                  url(r'^lesson/$', views.lesson_list, name='lesson_list'),
                  url(r'^elesson/(?P<pk>\d+)/$', views.lesson_edit, name='edit lesson'),
                  url(r'^add_lesson/$', views.add_lesson, name='add_lesson')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
