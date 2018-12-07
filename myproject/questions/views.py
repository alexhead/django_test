# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import resolve_url
from django.views.generic import DetailView
from django.views.generic import CreateView, ListView
from .models import Quest
from .forms import QuestListForm, QuestForm 

class QuestView(DetailView):
    model = Quest
    template_name = 'quest_detail.html'
    content_object_name = 'quest'
class QuestView(CreateView):
    model = Quest
    template_name = 'create.html'
    fields = ('title', 'text', 'sub_text')
    def get_success_url(self):
        return resolve_url('questions:quest_detail', pk=self.object.pk)
    

class QuestList(ListView):
    model = Quest
    template_name = 'quest_list.html'
    content_object_name = 'quest'

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestListForm(request.GET)
        self.form.is_valid()
        self.qform = QuestForm(request.POST or None)
        return super(QuestList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Quest.objects.all()
        if self.form.cleaned_data.get('search'):
           queryset = queryset.filter(title = self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
	       queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:3]
        return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['qform'] = self.qform
        return context
