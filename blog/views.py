from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import CommentForm
from .models import Comment

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render( request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'form': form})