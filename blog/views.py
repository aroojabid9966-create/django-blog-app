from django.shortcuts import render,get_object_or_404,redirect
from . models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django .contrib.auth.forms import UserCreationForm
from django.contrib import messages
@login_required
def create_blog(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('blog_list')
    else:
        form=BlogForm() 
    return render(request,'create_blog.html',{'form':form})
@login_required
def blog_list(request):
    blogs=Blog.objects.all()  
    return render(request,'blog_list.html',{'blogs':blogs})
def blog_detail(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    return render(request,'blog_detail.html',{'blog':blog})
@login_required
def edit_blog(request,slug):
    
    blog=get_object_or_404(Blog,slug=slug)
    if blog.author!=request.user:
        return redirect('blog_list')
    if request.method == 'POST':
       form=BlogForm(request.POST,instance=blog)
       if form.is_valid():
          form.save()
          return redirect('blog_detail',slug=slug)
    else:
        form = BlogForm(instance=blog)   
    return render(request,'edit_blog.html',{'form':form})
@login_required
def del_blog(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    if blog.author!=request.user:
        return redirect('blog_list')
    blog.delete()
    return redirect('blog_list')
@login_required
def page_profile(request):
    blogs=Blog.objects.filter(author=request.user)
    return render(request,'profile.html',{'blogs':blogs})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created!')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})


    
    
    


    



    
