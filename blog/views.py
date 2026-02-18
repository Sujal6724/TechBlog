from django.shortcuts import render
from .models import BlogPost


def blog_list(request):
	posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
	return render(request, 'blog/blog_list.html', {'posts': posts})


# Different QuerySet Examples
# All posts
# BlogPost.objects.all()

# Filter by category
# BlogPost.objects.filter(category='DJ')

# Get single object
# BlogPost.objects.get(id=1)

# Exclude unpublished
# BlogPost.objects.exclude(is_published=False)

# Count posts
# BlogPost.objects.count()

# Latest post
# BlogPost.objects.latest('created_at')
