from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),
)
