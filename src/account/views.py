from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from account.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'account/index.html', {'form': form})
