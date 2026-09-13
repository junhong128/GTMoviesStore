from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required

def signup(request):
    template_data = {}
    template_data['title'] = 'Register'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.signin')
        else:
            template_data['form'] = form
            return render(request, 'signup.html',
                {'template_data': template_data})

def signin(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'signin.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'signin.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('movies.index')

@login_required
def signout(request):
    auth_logout(request)
    return redirect('landing')