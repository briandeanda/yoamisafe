from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^yo', include('yoamisafe.urls', namespace='yoamisafe')),
    url(r'^/admin/', include(admin.site.urls)),
)
