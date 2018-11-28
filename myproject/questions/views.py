# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Quest 

class QuestView(DetailView):
    model = Quest
    template_name = 'quest_detail.html'
    context_object_name = 'quest'

class QuestList(ListView):
    model = Quest
    template_name = 'quest_list.html'
    content_object_name = 'quest'

    def dispatch(self, request, *args, **kwargs):
        self.search = request.GET.get('Search')
        self.sort_field = request.GET.get('Sort_field')
        return super(QuestList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Quest.objects.all()
	if self.search:
        	queryset = queryset.filter(title = self.search)
	if self.sort_field:
		queryset = queryset.order_by(self.sort_field)[:3]
	return queryset
