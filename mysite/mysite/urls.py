from django.conf.urls import patterns, include, url
#from mysite.views import hell
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'mysite.views.login'),   
   url(r'^accounts/auth/$', 'mysite.views.auth_view'),
   url(r'^accounts/logout/$', 'mysite.views.logout'),
    url(r'^accounts/loggedin/$','mysite.views.loggedin'),
   url(r'^accounts/invalid/$','mysite.views.invalid_login'),
   url(r'^accounts/register/$','mysite.views.register_user'),
   url(r'^accounts/register_success/$','mysite.views.register_success'),
   url(r'^accounts/forgot_password/$','mysite.views.UserResetPassword'),
    url(r'^accounts/confirm/$', 'mysite.views.confirm'),
   url(r'^search-form/$', 'books.views.search_form'),
   #url(r'^articles/all/$', 'books.views.search_form'),
   url(r'^search/$', 'books.views.search'),
   url(r'^contact/$', 'books.views.contact'),
   url(r'^contact/thanks/$', 'books.views.contact_thanks'),
   url(r'^articles/',include('books.urls')),
    url(r'^about/$', 'books.views.about'),
    url(r'^$', 'books.views.about'),
   
)

