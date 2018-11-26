from django.conf.urls import url
from .views import QuestionsView

app_name = 'questions'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', QuestionsView.as_view(), name='quest_detail'),
	]
