# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Quest(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add = True)
    sub_text = models.TextField()
    
    def __unicode__(self):
        return self.title

    class Meta:
	verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'	
