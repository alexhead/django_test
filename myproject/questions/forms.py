# -*- coding: utf-8 -*-
from django import forms

class QuestListForm(forms.Form):
	search = forms.CharField(required=False)
	sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('created_at', 'Дата')), required=False)

class QuestForm(forms.Form)
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	sub_text = forms.CharField(widget=forms.Textarea)

