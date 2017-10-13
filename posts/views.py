from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from .forms import PostForm, CommentForm
from .models import Post, Profile, Comment, SubComment


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/index.html', {'post_list': post_list})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'posts/post.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            profile = Profile.objects.all()[0]
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.pub_date = timezone.now()
            post.author = profile
            post.save()
            return HttpResponseRedirect(reverse('posts:index'))
        return HttpResponse('WTF POST')
    else:
        return HttpResponseRedirect('WTF METHOD')


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.post = get_object_or_404(Post, pk=post_id)
            comment.comment_owner = form.cleaned_data['comment_owner']
            comment.comment = form.cleaned_data['comment']
            comment.comment_date = timezone.now()
            comment.save()
            return HttpResponseRedirect(reverse('posts:post', kwargs={'post_id': post_id}))
        else:
            return HttpResponse(form)
    else:
        return HttpResponseRedirect('WTF')


def post_form(request, post_id):
    #    post = get_object_or_404(Post, pk=post_id)
    #    form = PostForm(initial={
    #        'title': post.title,
    #        'text': post.text
    #    })

    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'post_id': post_id})


def update_post(request, post_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=post_id)
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.save()
            return HttpResponseRedirect(reverse('posts:post', kwargs={'post_id': post_id}))
        return HttpResponse('WTF FORM')
    else:
        return HttpResponse('WTF METHOD')


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('posts:index'))


def my_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        return HttpResponse("WTF LOGIN.")


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')
