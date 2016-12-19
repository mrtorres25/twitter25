"""twitteranalytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls')),
    url(r'^login/', 'users.views.login', name = 'login'),
    url(r'^logout/', 'users.views.logout', name = 'logout'),
    url(r'^searchurl/', include('searchByUrl.urls')),
    url(r'^location/', include('location.urls')),
    url(r'^geosearch/', include('geosearch.urls'), name = 'geosearch'),
    url(r'^$', 'users.views.login', name = 'home'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
