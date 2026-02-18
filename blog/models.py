from django.db import models

class BlogPost(models.Model):
	CATEGORY_CHOICES = [
		('PY', 'Python'),
		('DJ', 'Django'),
		('JS', 'JavaScript'),
		('AI', 'Artificial Intelligence'),
	]

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	content = models.TextField()
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
