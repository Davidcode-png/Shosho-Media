from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView,RedirectView
from .models import Post,Comment,Profile
from .forms import PostForm,CommentForm

class PostListView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        loggedin_user = request.user
        posts = Post.objects.filter(
            author__profile__followers__in = [loggedin_user.id]
        ).order_by('-created_on')
        form = PostForm()
        context = {'post_list':posts,'form':form}
        return render(request,'shosho/post_list.html',context)
    
    def post(self,request,*args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        context = {'post_list':posts,'form':form}
        #return render(request,'shosho/post_list.html',context)
        #return super(PostListView, self).dispatch(request, *args, **kwargs)
        return redirect('post-list')

class PostDetailView(LoginRequiredMixin, RedirectView,View):
    def get(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {'post':post,'form':form,'comments':comments}
        return render(request,'shosho/post_detail.html',context)
    
    def post(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {'post':post,'form':form,'comments':comments}
        #return render(request,'shosho/post_detail.html',context)
        return redirect('post-detail',pk=post.id)


class PostEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['body']
    template_name = 'shosho/post_edit.html'
    
    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail',kwargs = {'pk':pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'shosho/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = 'shosho/comment_delete.html'
    def get_success_url(self) -> str:
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail',kwargs = {'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class ProfileView(View):
    def get(self,request,pk,*args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        followers = profile.followers.all()
        no_of_followers = len(followers)
        is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        context = {'user':user,'profile':profile,'posts':posts,'no_of_followers':no_of_followers,'is_following':is_following,}
        return render(request,'shosho/profile.html',context)


class ProfileEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Profile
    fields = ['name','birth_date','bio','location','picture']
    template_name = 'shosho/profile_edit.html'
    
    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        return reverse_lazy('profile',kwargs = {'pk':pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

class AddFollower(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)
        return redirect('profile',pk=profile.pk)

class RemoveFollower(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return redirect('profile',pk=profile.pk)

class AddLike(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class Dislike(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class UserSearch(View):
    def get(self,request,*args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)
        )
        context = {'profile_list':profile_list}
    
        return render(request,'shosho/search.html',context)