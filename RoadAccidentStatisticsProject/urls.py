from django.conf.urls import patterns, include, url
from RoadAccidentStatistics.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hierarchy/', render_object_hierarchy),
    url(r'^dashboard/', dashboard),
    url(r'^bubble_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})/data', bubble_chart_data),
    url(r'^bubble_chart/regions/([\w ,]+)/from_year/(\d{4})/to_year/(\d{4})', bubble_chart_url),
    url(r'^bubble_chart/', bubble_chart),
)
urlpatterns += staticfiles_urlpatterns()
