from django.conf.urls import url
from .views import QuestView
from .views import QuestList

app_name = 'questions'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', QuestView.as_view(), name='quest_detail'),
    url(r'^(list/$', QuestView.as_view(), name='quest_detail'),
	]
