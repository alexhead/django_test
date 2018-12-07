from django.conf.urls import url
from .views import QuestView
from .views import QuestList
from .views import CreateQuest

app_name = 'questions'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', QuestView.as_view(), name='quest_detail'),
    url(r'^list/$', QuestList.as_view(), name='quest_list'),
    url(r'^list/create/$', CreateQuest.as_view(), name="create"),
	]
