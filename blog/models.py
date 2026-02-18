from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
	CATEGORY_CHOICES = [
		('PY', 'Python'),
		('DJ', 'Django'),
		('JS', 'JavaScript'),
		('AI', 'Artificial Intelligence'),
	]

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True)
	author = models.CharField(max_length=100)
	content = models.TextField()
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
