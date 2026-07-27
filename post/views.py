from django.shortcuts import render, redirect , get_object_or_404
from .models import BlogPost
from .forms import BlogForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self,request):
        post_list = BlogPost.objects.order_by("-creation_date")
        return render(request,"post/index.html",{ "post_list" : post_list})
    
class CreatePostView(LoginRequiredMixin,View):
    login_url = "account:login"
    
    def get(self, request):
        form = BlogForm()
        return render(request,"post/create.html",{"form" : form})
    
    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:index")
        else:
            return render(request,"post/create.html",{"form" : form})
        
class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(BlogPost, id=id)
        return render(request,"post/post_detail.html",{ "post" : post })
        
    
    
index = IndexView.as_view()
create = CreatePostView.as_view()
detail = PostDetailView.as_view()