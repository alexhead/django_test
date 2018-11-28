# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Quest
from .forms import QuestListForm 

class QuestView(DetailView):
    model = Quest
    template_name = 'quest_detail.html'
    context_object_name = 'quest'

class QuestList(ListView):
    model = Quest
    template_name = 'quest_list.html'
    content_object_name = 'quest'

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestListForm(request.GET)
        self.form.is_valid()
        return super(QuestList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Quest.objects.all()
	    if self.form.cleaned_data.get('Search'):
            queryset = queryset.filter(title = self.form.cleaned_data['Search'])
	    if self.sort_field:
		    queryset = queryset.order_by(self.form.cleaned_data['Sort_field'])[:3]
	    return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context
