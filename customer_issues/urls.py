from django.conf.urls import patterns, include, url
from django.contrib import admin

from issues.views import home 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'customer_issues.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$' , home),
)
