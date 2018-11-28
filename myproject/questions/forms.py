# -*- coding: utf-8 -*-
from django import forms

class QuestListForm(forms.Form):
	search = forms.CharField(required=False)
	sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('created_at', 'Дата')), required=False)

	def clean_search(self):
		clean = self.cleaned_data.get('Search')
		raise forms.ValidationError(u'Неправильный поиск')
		return search
