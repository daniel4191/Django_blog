from datetime import date
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm


class StartPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


'''
# 위의 class StartPageView로 대체되었다.
def starting_page(request):
    # -date를 이용해서 DESC 정렬
    latest_posts = Post.objects.all().order_by('-date')[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })
'''


class AllPostView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


'''
# 위의 AllPostView로 대체되었다.
def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/posts.html", {
        'all_posts': all_posts
    })
'''


def get_date(post):
    # 위의 딕셔너리 중 date라는 키값을 얻어주는 것이다.
    return post.get('date')
# Create your views here.


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post_detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # reverse에 들어가는 인자는 urls.py의 name으로부터 비롯되었음
            return HttpResponseRedirect(reverse('post_detail_page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            # 'comment_form': CommentForm()
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_saved_for_later(request, post.id)
        }
        return render(request, 'blog/post_detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {

        }

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        # POST의 인자 post_id는 post_detail.html의 name으로 지정된 것에서 비롯된다.
        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')


'''
# 인자가 DetailView일때 사용하는 정의
class SinglePostView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context
'''

'''
# 위의 SinglePostView로 대체되었다.
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': identified_post,
        # post_detail.html로 보내는 값이다.
        'post_tags': identified_post.tags.all()
    })
'''
