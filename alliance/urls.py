from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('alliance.views',
    url(r'^$', 'front_page'),

    url(r'^users/(?P<username>.+)/$', 'user_profile'),

    # Putting database primary keys in the URL isn't exactly pretty,
    # but it'll do for now
    url(r'^opportunities/(?P<pk>.+)/$', 'opportunity'),
)
