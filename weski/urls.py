from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'weski.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^tripbuilder/', include('tripbuilder.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
