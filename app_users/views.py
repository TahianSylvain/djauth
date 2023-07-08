from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import SignUpUserForm, UserProfileInfoForm
from app_users.models import UserProfile


# @login_required(login_url='account:login')
def dashboard(request):  # workspace
    return render(request, 'app_users/workspace.html', context={
        'hi': str('Hello, world!'),
    })


def register(request):
    if request.method == 'POST':
        user_form = SignUpUserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # there is a user_mail confirmation first
            user = user_form.save()
            # user.email_user()
            user.save()
            print(profile_form)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = SignUpUserForm()
        profile_form = UserProfileInfoForm()

    if 'Male' == UserProfile.gender:
        male = True
    else:
        male = False

    return render(request, 'app_users/sign_up.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
        'male': not male
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('account:workspace'))
            else:
                return HttpResponse('Account is deactivated!')
        else:
            return HttpResponse('Please, Use correct name or password!')
    else:
        return render(request, 'app_users/log_in.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:gate'))


def display_widgets(request):  # gate
    return render(request, 'app_users/get_to_site.html',
                  {
                      'some': 'All the SPONSORING & Blog & publicity to display!'
                  })
