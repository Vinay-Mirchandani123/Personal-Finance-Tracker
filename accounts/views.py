from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib import messages
from .models import Profile
from .forms import UserProfileForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
       return render(request, 'index.html')
    return render(request, 'accounts/login.html')

def loginUser(request):
    
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']

        user = User.objects.filter(username = email)
        
        if not user.exists():
            messages.warning(request, "Account not Found")
            return HttpResponseRedirect(request.path_info)
        
        if not user[0].profile.email_verified:
            messages.warning(request, "Email not verified")
            return HttpResponseRedirect(request.path_info)

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return render(request, "mainbase.html")
        
        messages.success(request, "Invalid Credentials")
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/login.html')

def profile_edit(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {'form': form})

def logoutUser(request):
    logout(request)
    # messages.success(request, "Your Account has been Sucessfully Logged out")
    return redirect("login")

def register(request):
    if(request.method=="POST"):
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        password=request.POST['password']
        conpassword=request.POST['conpassword']

        #check pass and conpass are same
        if(password!=conpassword):
            messages.warning(request, "Confirm Password should be same as Original Password")
            return HttpResponseRedirect(request.path_info)


        user = User.objects.filter(username = email)
        
        if user.exists():
            messages.warning(request, "Email already exist")
            return HttpResponseRedirect(request.path_info)
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name= firstName
        user.last_name = lastName
        user.save()
        messages.success(request, "Your Account has been Successfully Created")
        return HttpResponseRedirect(request.path_info)
   
    return render(request, 'accounts/register.html')
