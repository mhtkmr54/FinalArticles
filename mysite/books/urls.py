from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','books.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$','books.views.article'),
    url(r'^create/$', 'books.views.create'),
    url(r'^like/(?P<article_id>\d+)/$','books.views.like_article'),
    #url(r'^unlike/(?P<article_id>\d+)/$','books.views.unlike_article'),
    
    
)