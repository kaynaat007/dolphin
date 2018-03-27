# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

UPVOTE = 1
DOWNVOTE = -1

VOTE_CHOICES = (
    (UPVOTE, 'UPVOTE'),
    (DOWNVOTE, 'DOWNVOTE')
)


class User(models.Model):
    """
    This is user table.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=1023)

    def __str__(self):
        return self.username


class Question(models.Model):
    """
    The questions.
    """
    statement = models.CharField(max_length=2 * 1023)
    asked_by = models.ForeignKey(User)
    asked_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statement


class Answer(models.Model):
    """
    The answers. One question can have many answers
    """
    statement = models.CharField(max_length=2 * 1023)
    answered_at = models.DateTimeField(auto_now=True)
    answered_by = models.ForeignKey(User)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.statement


class Vote(models.Model):
    """
    The vote count model. who voted which answer and when.
    """
    answer = models.ForeignKey(Answer)
    voted_by = models.ForeignKey(User)
    voted_at = models.DateTimeField(auto_now=True)
    weight = models.IntegerField(choices=VOTE_CHOICES)

    def __str__(self):
        return '{1} voted by {0} for answer id {2}'.format(self.voted_by.username, self.weight, self.answer.pk)


