from yoamisafe import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    url(r'yoamisafe?username=(?P<username>\D+)&location=(?P<longitude>\D+);(?P<latitude>\D+)$', views.map, name='map'),
    url(r'/temp', views.temp, name='temp'),

)