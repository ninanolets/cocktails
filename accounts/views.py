from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from posts.models import Post

def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)    
        form = UserRegisterForm(request.POST)    
        if form.is_valid():
            form.save()

            # user = form.cleaned_data.get('first_name')
            # if not user:
            #     user = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {user}')
            messages.success(request, f'Your account has been created. You can Log In now.')
            return redirect('login')

    else:
        # form = UserCreationForm()
        form = UserRegisterForm()

    context = { 'form': form }
    return render(request, 'accounts/register.html', context)

@login_required
def profile(request):
    posts = Post.objects.filter(user_id=request.user)

    context = { 'posts': posts }

    return render(request, 'accounts/profile.html', context)

@login_required
def update_profile(request):
    # the arguments can be passed bc of forms.ModelForm
    
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        # the arguments make sure the previous data is already filled out
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { 
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'accounts/update_profile.html', context)

