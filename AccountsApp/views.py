from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AccountsApp.models import CustomUser as User       


# Create your views here.

########################################################
##################   TEST VIEWS   ######################
########################################################

def temp_test(request):
    return render(request, 'base.html')

def test(request):
    return render(request, 'test.html')
############   END OF TEST VIEWS    ##################


#######################################################################
###########################  LOGIN VIEW    ############################
#######################################################################
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('RestApp:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username != '' and password  != '':
                user = authenticate(username = username, password = password)
                
                if user is not None:
                    login(request, user)
                    return redirect('RestApp:home')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('AccountsApp:login')
            else:
                messages.info(request, 'username and password cannot be empty')
                return redirect('AccountsApp:login')
                
        else:
            print('Not a Post method')
            return render(request, 'AccountsApp/auth-login.html')
##############  END OF LOGIN VIEW    ###############################



#######################################################################
######################   LOGOUT VIEW      #############################
#######################################################################
@login_required(login_url='/')
def LogoutView(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('AccountsApp:login')
###################   END OF LOGOUT VIEW   ##########################


#######################################################################
######################   CHANGE PASSWORD VIEW      ####################
#######################################################################
@login_required(login_url='/')
def ChangePaswordView(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(password, confirm_password)
        if password != '':
            if password == confirm_password:                
                user.set_password(password)
                user.save()
                login(request, user)
                messages.info(request, 'Password Changed Successfuly')
                return redirect('RestApp:dashboard')

            else:
                messages.info(request, 'Passwords not matched')
                return redirect('AccountsApp:change-password', user.id)
        else:
            messages.info(request, 'Password cannot be empty')
            return redirect('AccountsApp:change-password', user.id)
    else:
        return render(request, 'AccountsApp/auth-change-password.html')
            

        
        

