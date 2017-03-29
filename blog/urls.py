from django.conf.urls import url
from . import views
from .views import AuthorsView

urlpatterns = [
    url(r'^$', views.list_posts, name='index'),
    
    url(r'^blog/$', views.list_posts, name='list_posts'),
    url(r'^blog/category/(?P<slug>[^\.]+)/$', views.list_posts_category, name='list_posts_category'),
    url(r'^post/(?P<slug>[^\.]+)/$', views.view_post, name='view_post'),    
    
    url(r'^authors/$', AuthorsView.as_view(), name='list_authors'),
    url(r'^author/(?P<slug>[^\.]+)/(?P<demography>[^\.]+)/$', views.view_author, name='view_author_demography'),
    url(r'^author/(?P<slug>[^\.]+)/$', views.view_author, name='view_author'),
        
    url(r'^publishers/$', views.list_publishers, name='list_publishers'),
    url(r'^publisher/(?P<slug>[^\.]+)/(?P<demography>[^\.]+)/$', views.view_publisher, name='view_publisher_demography'),
    url(r'^publisher/(?P<slug>[^\.]+)/$', views.view_publisher, name='view_publisher'),
    
    url(r'^series/genre/(?P<genre>[^\.]+)/$', views.list_series_genre, name='list_series_genre'),
    url(r'^series/(?P<demography>[^\.]+)/$', views.list_series, name='list_series_demography'),
    url(r'^series/$', views.list_series, name='list_series'),
    url(r'^serie/(?P<slug>[^\.]+)/$', views.view_serie, name='view_serie'),
    
    url(r'^announcements/$', views.list_announcements, name='list_announcements'),
    url(r'^announcements/(?P<year>[^\.]+)/$', views.list_announcements, name='list_announcements_year'), #limit 4
    
    url(r'^calendar/$', views.list_volumes, name='list_volumes'),
    url(r'^calendar/(?P<year>[^\.]{4})/(?P<month>[^\.]{1,2})/$', views.list_volumes, name='list_volumes_month'), #limit 4, 2
    
    url(r'^links/$', views.list_links, name='list_links'),
]

