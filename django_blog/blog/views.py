from django.contrib.auth.forms import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .models import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm

# View to display a post and its comments
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", post_id=post.id)

    return render(request, "blog/post.html", {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

# Edit comment view
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user != comment.author:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {'form': form, "comment": comment})

# Delete comment view
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    post_id = comment.post.id
    comment.delete()
    return redirect("post_detail", post_id=post_id)

# List View - show all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post"

# Detail view - show the single post of the user
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create view - create a new post which allows authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user # Automatically set the current user as author
        return super().form_valid(form)
    
# Update view - allows only the author to edit a post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
      post = self.get_object()
      return self.request.user == post.author
    
# Delete view - allows only the author to delete a post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = CustomUserCreationForm()
            return render(request, "blog/register.html", {"form":form})
    
# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home") # Redirect to homepage after login
        else:
            form = AuthenticationForm()
            return render(request, "blog/login.html", {"form":form})
        
# User Logout 
def user_logout(request):
    logout(request)
    return redirect("login")

# User Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")
