from django.conf.urls.defaults import *
from entries.models import Entry

info_dict = {
    'queryset':Entry.objects.all(),
    }

urlpatterns = patterns('',
    (r'^$',
    # select
    'django.views.generic.list_detail.object_list',
    info_dict),
    # create
    (r'^create/$',
    'django.views.generic.create_update.create_object',
    {'model':Entry, 'post_save_redirect':'/entries/'}),
    # edit
    (r'^detail/(?P<object_id>\d+)/$',
    'django.views.generic.list_detail.object_detail',
    info_dict),
    # update
    (r'^update/(?P<object_id>\d+)/$',
    'django.views.generic.create_update.update_object',
    {'model':Entry}),
    # delete
    (r'^delete/(?P<object_id>\d+)/$',
    'django.views.generic.create_update.delete_object',
    {'model':Entry, 'post_delete_redirect':'/entries/'}),
)

# login / logout
urlpatterns += patterns('',
                       (r'login/$', 'django.contrib.auth.views.login',
                         {'template_name':'entries/registration/login.html'}),
                       (r'^logout/$',
                         'django.contrib.auth.views.logout',
                         {'template_name':'entries/registration/logout.html'}),
                       )
