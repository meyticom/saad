from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from portal import views

urlpatterns = [
                  url(r'^teacher/(?P<pk>\d+)/$', views.edit_teacher, name='teacher'),
                  url(r'^teachers', views.view_teacher, name='teachers'),
                  url(r'^teacher/(?P<pk>\d+)/del/$', views.del_teacher, name='del_teacher'),
                  url(r'^add_student/$', views.add_student, name='add_student'),
                  url(r'^add_teacher/$', views.add_teacher, name='add_teacher'),
                  url(r'^students/$', views.all_student, name='students'),
                  url(r'^student/(?P<pk>\d+)/del/$', views.del_student, name='del_student'),
                  url(r'^student/(?P<pk>\d+)/$', views.edit_student, name='edit_student'),
                  url(r'^lessons/$', views.lesson_list, name='lessons'),
                  url(r'^lesson/(?P<pk>\d+)/$', views.lesson_edit, name='edit_lesson'),
                  url(r'^lesson/(?P<pk>\d+)/del/$', views.del_lesson, name='del_lesson'),
                  url(r'^add_lesson/$', views.add_lesson, name='add_lesson'),
                  url(r'^setting/$', views.setting, name='setting'),
                  url(r'^login/$', views.user_login, name='login'),
                  url(r'^logout/$', views.user_logout, name='logout'),
                  #url(r'^', views.add_student, name='add_student'),# amele baz nashodan aksha

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)