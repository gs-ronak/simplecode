from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse("tag_index", kwargs={"slug": self.slug})
