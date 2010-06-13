from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from hub_users.forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #request.POST['username']
            password = form.cleaned_data['password'] #request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
                else:
                    messages.warning(request, 'Your account has been disabled')
            else:
                messages.warning(request, 'Invalid account')
    else:
        form = LoginForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'hub_users/login.html',
        data,
        context_instance=RequestContext(request),
    ) 

def user_logout(request):
    logout(request)
    return redirect('hub-users:login')
