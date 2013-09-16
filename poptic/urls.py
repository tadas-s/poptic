from django.conf.urls import patterns, include, url
from poptic.apps.front.event.views import EventListView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'poptic.views.home', name='home'),
    # url(r'^poptic/', include('poptic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', EventListView.as_view(), name='event-list'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^new$', contacts.views.Create1ContactView.as_view(), name='event-view')
)
