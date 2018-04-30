from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^clublist$', views.post_list_full, name='post_list_full'),
    url(r'^myclubs$', views.my_clubs, name='my_clubs'),
    url(r'^search/$', views.search),
    url(r'^login$', views.login, name='login'),
    url(r'^post/new/(?P<pk>\d+)/$', views.post_new, name='post_new'),
    url(r'^review/(?P<pk>\d+)/$', views.review_detail, name='review_detail'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')), #app_name='ratings')),
    url(r'^review/(?P<pk_Club>\d+)/(?P<pk_Review>\d+)/inc/$', views.review_increment, name='review_increment'),
    url(r'^review/(?P<pk_Club>\d+)/(?P<pk_Review>\d+)/dec/$', views.review_decrement, name='review_decrement'),
    url(r'^top20$', views.top20, name='top20'),
    url(r'^review/(?P<pk>\d+)/allreviews$', views.all_reviews, name='all_reviews'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.edit_page, name='edit_page'),
    url(r'^post/interest/(?P<pk>\d+)/$', views.interest_page, name='interest_page'),
]
