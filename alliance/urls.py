from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('alliance.views',
    url(r'^$', 'front_page'),
)
