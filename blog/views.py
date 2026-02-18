from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import BlogPost


def blog_list(request):
	posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


def blog_detail(request, slug):
	post = get_object_or_404(BlogPost, slug=slug, is_published=True)
	return render(request, 'blog/blog_detail.html', {'post': post})


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
