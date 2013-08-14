from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jam.views.home', name='home'),
    # url(r'^jam/', include('jam.foo.urls')),
    url(r'^entries/', include('entries.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/',  include(admin.site.urls)),
)

from django.conf import settings
import os

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)',
                             'django.views.static.serve',
                             {'document_root':settings.STATIC_ROOT,
                             'show_indexes':True}),
                             #{'document_root': settings.MEDIA_URL +
                             #{'document_root' : os.path.dirname(__file__) +
                             # '/static'}),
                            )
