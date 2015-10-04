from django.conf.urls import include, url

from views import viewForums, viewSingleForum, viewSingleThread, viewComment

urlpatterns = [
    url(r'^$', viewForums, name='viewForums'),
    url(r'^(?P<forum_id>[0-9]+)/$', viewSingleForum, name='viewSingleForum'),
    url(r'^thread/(?P<thread_id>[0-9]+)/$', viewSingleThread, name='viewSingleThread'),
]

