from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import haystack
haystack.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoblogproject.views.home', name='home'),
    url(r'^', include('djangoblogproject.blogengine.urls')),
    
    url(r'^hitcounter', include('djangoblogproject.hitcounter.urls')),
    
    url(r'^subscribe', include('djangoblogproject.subscribe.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'F:/MySource/djangoblogproject/templates/static'},),
)

urlpatterns += patterns('',
    url(r'^pages', include('django.contrib.flatpages.urls')),
)
