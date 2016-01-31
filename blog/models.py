from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
import markdown2


class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField('Tag')
	body_html = models.TextField(editable=False, blank=True, null=True)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	def save(self):
		self.body_html = markdown2.markdown(self.body, extras=['fenced-code-blocks'])
		super(Entry, self).save()
	
	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-date_created"]

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse("tag_index", kwargs={"slug": self.slug})


