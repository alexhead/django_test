from django.conf.urls import url
from .views import NewsView


app_name = 'news'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name='detail'), 
    url(r'^(?P<pk>\d+)/hello/$', news.views.show_news, name='detail_show'),   
 ]
