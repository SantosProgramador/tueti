from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tuet(models.Model):
	text = models.CharField(max_length=140)
	author = models.ForeignKey('TuetiUser')
	response_to = models.ForeignKey('Tuet', blank=True, null=True)
	created = models.DateTimeField(default=timezone.now)
	liked_by = models.ManyToManyField(User, blank=True, related_name='liked_tuets')

	def is_comment(self):
		return bool(response_to)


class TuetiUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('TuetiUser', blank=True, related_name="followed_by")