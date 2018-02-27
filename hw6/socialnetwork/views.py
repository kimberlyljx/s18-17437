# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.db import transaction
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.conf import settings

from socialnetwork.models import Post, Profile
from socialnetwork.forms import RegistrationForm, PostForm, CommentForm, EditProfileForm

@login_required
def home(request):
    entries = Post.objects.order_by('-creation_time')
    comment_form = CommentForm()
    post_form = PostForm()
    if request.method == "POST":
        if request.POST.get("wall_post"):
            new_post = Post(user_profile=request.user.profile, creation_time=timezone.now())
            post_form = PostForm(request.POST, instance=new_post)
            if not post_form.is_valid():
                messages.error(request, "Your post has errors")
            else:
                post_form.save()
                messages.success(request, "Your post has been made")
                return redirect(reverse('home'))
        elif request.POST.get("comment"):
            comment_form = CommentForm(request.POST)
            if not comment_form.is_valid():
                messages.error(request, "Your comment has errors")
            else:
                messages.success(request, "Your comment has been made")
                return redirect(reverse('home'))
    context = {'entries': entries, 'form': comment_form, 'post_form': post_form}
    return render(request, 'socialnetwork/stream.html', context)

@login_required
def follower(request):
    my_follows = request.user.profile.follows.all()
    entries = Post.objects.filter(user_profile__in=my_follows).order_by('-creation_time')
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if not comment_form.is_valid():
            messages.error(request, "Your comment has errors")
        else:
            messages.success(request, "Your comment has been posted")
            return redirect(reverse('follower'))   
    context = { 'entries': entries, 'form': comment_form }
    return render(request, 'socialnetwork/stream.html', context)

@login_required
@transaction.atomic
def other(request, id):
    # be sure to line below works as per grade comment
    profile = get_object_or_404(Profile, id=id)
    follows = profile.follows.all()
    my_follows = request.user.profile.follows.all()
    if request.method == 'POST':
        if profile in my_follows:
            request.user.profile.follows.remove(profile)
            messages.info(request, "You've unfollowed " + profile.user.username)
        else:
            request.user.profile.follows.add(profile)
            messages.info(request, "You've followed " + profile.user.username)
        request.user.profile.save()
        return redirect(reverse('other', args=id))
    follow_status = 'Unfollow' if profile in my_follows else 'Follow'
    context = {'follows': follows, 'profile': profile, 'follow_status' : follow_status}
    return render(request, 'socialnetwork/other.html', context)

@login_required
@transaction.atomic
def profile(request):
    follows = request.user.profile.follows.all()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        old_profile = request.user.profile.picture
        if form.is_valid():
            request.user.profile.content_type = form.cleaned_data['picture'].content_type
            if (old_profile != settings.DEFAULT_PIC): old_profile.delete()
            request.user.profile.picture = form.cleaned_data['picture']
            request.user.profile.save()
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect(reverse('profile'))
        else:
            messages.error(request, "Your update was invalid")
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'socialnetwork/profile.html', {'profile_form': form, 
        'follows': follows})

@transaction.atomic
def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'socialnetwork/register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'socialnetwork/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save();

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
    login(request, new_user)
    return redirect(reverse('home'));

@login_required
def get_photo(request, id):
    profile = get_object_or_404(Profile, id=id)

    # Probably don't need this check as form validation requires a picture be uploaded.
    if not profile.picture:
        raise Http404

    return HttpResponse(profile.picture, content_type=profile.content_type)
