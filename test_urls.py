from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^notices/', include('letterbox.urls')),
)
