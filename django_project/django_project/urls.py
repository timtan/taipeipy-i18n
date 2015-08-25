from django.conf.urls import patterns, include, url
from django.contrib import admin
from sample.views import index
from django.views.i18n import javascript_catalog


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^jsi18n/$', javascript_catalog, ),
                       url(r'^admin/', include(admin.site.urls)),
                       )
