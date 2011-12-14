from django.conf.urls.defaults import patterns, url

from django.views.generic import DetailView

from letterbox.models import Notice
from letterbox.views import (
    archive_notice,
    notices,
    all,
    unread,
    archived
)

urlpatterns = patterns('',
    url(r'^$', notices, name='letterbox_notices'),
    url(r'^all/$', all, name='letterbox_all'),
    url(r'^archived/$', archived, name='letterbox_archived'),
    url(r'^unread/$', unread, name='letterbox_unread'),
    url(r'^(?P<pk>\d+)/$',DetailView.as_view(
        context_object_name="notice",
        model=Notice,
        template_name="letterbox/notice.html"
    ), name="letterbox_detail"),
    url(r'^archive/(?P<notice_id>\d+)/$',archive_notice, name='letterbox_archive'),
)
