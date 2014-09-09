from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'^notices/', include('letterbox.urls')),
)
