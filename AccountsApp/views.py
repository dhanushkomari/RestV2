from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def test(request):
    return render(request, 'test.html')



def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('RestApp:home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('AccountsApp:login')
    else:
        print('Not a Post method')
        return render(request, 'AccountsApp/login.html')

@login_required(login_url='/login')
def LogoutView(request):
    logout(request)
    return redirect('AccountsApp:login')
    

