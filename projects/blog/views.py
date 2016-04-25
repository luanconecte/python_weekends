from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .forms import PostForm

from .models import Post

from django.shortcuts import redirect

from django.contrib import messages

from django.core.urlresolvers import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):

	form = PostForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		post = form.save(commit=False)
		post.author_id = 1
		post.save()
		messages.success(request, 'Post created.')
		return redirect(reverse(post_create))

	return render(request, 'blog/post_create.html', { 'form': form })


@login_required
def posts(request, page=1):
	posts_list = Post.objects.all()
	paginator = Paginator(posts_list, 5) # Show 25 contacts per page
	posts = paginator.page(page)
	
	return render(request, 'blog/posts.html', { 'posts': posts, 'paginacao': paginacao(page, paginator.num_pages) })

def paginacao(atual=1, quantidade=1, intervalo=4):

	anterior = int(atual)-intervalo if int(atual)-intervalo >= 1 else 1
	proxima = int(atual)+(intervalo+1) if int(atual)+(intervalo+1) <= quantidade+1 else quantidade+1

	return {
		'atual': int(atual),
		'range': range(anterior, proxima)
	}

def post_edit(request, post):
	print request.method

	teste = get_object_or_404(Post, id=post)

	form = PostForm(request.POST or None, instance=teste)

	def post(self, *args, **kwargs):
		pass
	'''
	if request.method == 'POST' and form.is_valid():
		post = form.save(commit=False)
		post.author_id = 1
		post.save()
		messages.success(request, 'Post updated.')
		return redirect(reverse(posts))
	'''

	return render(request, 'blog/post_edit.html', { 'form': form })


class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy(posts)