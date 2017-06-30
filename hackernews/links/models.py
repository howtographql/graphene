# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    description = models.TextField()
    posted_by = models.ForeignKey('users.User', related_name='links')


class Vote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', related_name='votes')
    link = models.ForeignKey(Link, related_name='votes')
