from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('hitcounter.views',
    url(r'^(?P<website_url>(|https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)$)$', 'index'),
)