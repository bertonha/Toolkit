from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'Toolkit.views.home', name='home'),
    url(r'^sql/', include('sqlhelper.urls')),
)
