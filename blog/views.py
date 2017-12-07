from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from .forms import UserForm
from .forms import ProfileForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login
#from django.contrib.auth import authenticate

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/profile_temp.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def post_list(request):
	posts = Post.objects.order_by('created_date')
	return render(request, 'blog/title2.html', {'posts': posts})

def profile(request):
	#posts = Post.objects.order_by('created_date')
	#return render(request, 'blog/title.html', {'posts':posts})
	return render(request, 'blog/profile.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
	form = UserCreationForm(data=request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('post_list'))
	return render(request, 'blog/register.html', {'form': form})	
def test(request):
	return render(request, 'blog/title2.html')

	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})