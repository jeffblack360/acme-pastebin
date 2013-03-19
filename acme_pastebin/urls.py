from django.conf.urls import *
from django.views.generic import DetailView, ListView
from django.views.generic.create_update import create_object
from pastebin.models import Paste 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

display_info = {'queryset': Paste.objects.all()}
create_info  = {'model': Paste}

urlpatterns = patterns('',
    url(r'^$', object_list, dict(display_info, allow_empty=True)),
    url(r'^(?P<object_id>\d+)/$', object_detail, display_info),
    url(r'^add/$', create_object, create_info),

    # Examples:
    # url(r'^$', 'acme_pastebin.views.home', name='home'),
    # url(r'^acme_pastebin/', include('acme_pastebin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
