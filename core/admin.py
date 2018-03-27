# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import User, Question, Answer, Vote


class QuestionAdmin(admin.ModelAdmin):
    fields = ('statement', 'asked_by')


class AnswerAdmin(admin.ModelAdmin):
    fields = ('statement', 'answered_by', 'question')


class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'username', 'password')


class VoteAdmin(admin.ModelAdmin):
    fields = ('answer', 'voted_by', 'weight')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Vote, VoteAdmin)
