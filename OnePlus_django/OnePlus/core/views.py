from django.shortcuts import render,redirect
#new and alos redirect is new from above
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def test(request):
    return render(request,"core/base.html")

def navbar(request):
    return render(request,"core/navbar.html")

def footer(request):
    return render(request,"core/footer.html")

def products(request):
    return render(request,"core/products.html")

def contact(request):
    return render(request,"core/contact.html")

def cart(request):
    return render(request,"core/cart.html")

def account(request):
    return render(request,"core/account.html")

#Views for products on Homepage
def buds2(request):
    return render(request,"core/Buds_pro_2.html")

def nord_buds(request):
    return render(request,"core/nord_buds_2.html")

def bullets_z2(request):
    return render(request,"core/bullets_z2.html")

#Urls for products on Products page
def gaming_bundle(request):
    return render(request,"core/gaming_bundle.html")

def charging_bundle(request):
    return render(request,"core/charging_bundle.html")

def music_bundle(request):
    return render(request,"core/music_bundle.html")

def op_12r(request):
    return render(request,"core/op_12r.html")

def op_11r(request):
    return render(request,"core/op_11r.html")

def op_11_5g(request):
    return render(request,"core/op_11.html")

def pad_go(request):
    return render(request,"core/pad_go.html")

def op_pad(request):
    return render(request,"core/op_pad.html")

def folio_case(request):
    return render(request,"core/folio_case.html")

#signup request
def sign_up(request):
    if request.method == 'POST':
        mf = SignupForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/signup/')    
    else:
        mf  = SignupForm()
    return render(request,'core/signup.html',{'mf':mf})

#login request
def log_in(request):
    if not request.user.is_authenticated:  # check whether user is not login ,if so it will show login option
        if request.method == 'POST':       # otherwise it will redirect to the profile page 
            mf = AuthenticationForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/account/')
        else:
            mf = AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('/account/')

#profile
def profile(request):
    if request.user.is_authenticated:  # This check wheter user is login, if not it will redirect to login page
        return render(request,'core/account.html',{'name':request.user})
    else:                                                # request.user returns the username
        return redirect('/login/')


#logout
def log_out(request):
    logout(request)
    return redirect('/login/')

