from django.conf.urls import url, patterns


urlpatterns = patterns('sqlhelper.views',
    url(r'^insert/', 'insert', name='insert_sql'),
)
