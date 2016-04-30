from django.conf.urls import patterns, include, url
from django.contrib import admin

from issues.views import home 
from issues.views import add_issue, search, about, add_solution

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'customer_issues.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$' , home),
    url(r'^add/$', add_issue),
    url(r'^add_solution/$', add_solution),
    url(r'^search/$', search),
    url(r'^about/$', about),

)
