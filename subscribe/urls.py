from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('subscribe.views',
    url(r'^/$', 'index'),
    url(r'^/thanks/$', 'thanks'),
    url(r'^/subscribed-already/$', 'subscribed_already'),
    
    
    
)

