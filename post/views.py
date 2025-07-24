from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse


from django.shortcuts import render

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        "posts": posts
    })


def index1(request):
    return render(request, 'learn.html')

def index2(request):
    return render(request, 'pst.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')

    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = None

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, post=post, content=content)
        return redirect('post_detail', slug=post.slug)

    

class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return HttpResponseForbidden("Only Admin can perform this task")


class EditCommentView(LoginRequiredMixin,AdminOnlyMixin,UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug':self.object.post.slug})
    

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'  # Ensure this file exists

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user or self.request.user.is_superuser

