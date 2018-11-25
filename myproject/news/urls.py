from django.conf.urls import url
from .views import NewsView
from .views import show_news


app_name = 'news'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name='detail'),
    url(r'^(?P<news_id>\d+)/hello/$', show_news, name='detail_show'),

 ]
