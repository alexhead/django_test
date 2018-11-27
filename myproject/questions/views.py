# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from .models import Quest 

class QuestView(DetailView):
    model = Quest
    template_name = 'quest_detail.html'
    context_object_name = 'quest'

class QuestList(ListView):
	model = Quest
	template_name = 'quest_list.html'
	
