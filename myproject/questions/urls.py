from django.conf.urls import url
from .views import QuestView
from .views import QuestList
from .views import CreateView

app_name = 'questions'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', QuestView.as_view(), name='quest_detail'),
    url(r'^list/$', QuestList.as_view(), name='quest_list'),
    url(r'^list/create/$', CreateView.as_view(), name='create'),
	]
