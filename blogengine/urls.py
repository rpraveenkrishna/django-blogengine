from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('blogengine.views',
    (r'^$', 'home'),
    (r'^search/$', 'search'),
    (r'^blog/entry/(?P<slug_field>[^\.]+)/$', 'blog_entry_by_slug'),
    (r'^blog/category/(?P<slug_field>[^\.]+)/$', 'category_by_slug'),
)
