from django.conf.urls import re_path , url 
from . import views 
app_name = 'posts'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^posts/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^writers/$', views.WriterListView.as_view(), name='writers'),
    url(r'^profile/$', views.User_profile_view, name='profile'),
]
