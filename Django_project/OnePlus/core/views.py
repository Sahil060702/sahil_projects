from django.views import View
from .models import Customer,Product,Order,Cart
from . forms import AuthenticateForm,CustomerForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout,login as auth_login
from .forms import SignupForm,AuthenticateForm 
#===============For Paypal =========================
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
#=========================================================
# Create your views here.

def navbar(request):
    return render(request, 'core/navbar.html')

def aboutus(request):
    return render(request, 'core/about_us.html')

def cart(request):
    return render(request, 'core/cart.html')

def account(request):
    return render(request, 'core/login.html')

def login(request):
    return render(request,'core/login.html')

def products(request):
    product=Product.objects.all()
    return render(request, 'core/products.html',{'product':product})

def home(request):
        if  request.user.is_authenticated:
            product=Product.objects.filter(categories='home')
            return render(request,'core/home.html',{'product':product})
        else:
           return  redirect('/login/')
        


def log_in(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':       
            mf = AuthenticateForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    auth_login(request, user)
                    return redirect('/')
        else:
            mf = AuthenticateForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/login/')

def signup(request):
    if request.method == "POST":
        mf=SignupForm(request.POST)
   
        if mf.is_valid():
            mf.save()
            return redirect('/login/')
    else:
        mf=SignupForm()
    return render(request, 'core/signup.html', {'mf':mf})

    
class ProductDetailView(View):
    def get(self,request,id):     # id = It will fetch id of particular product 
        Product_detail = Product.objects.get(pk=id)

        #------ code for caculate percentage -----
        if Product_detail.discounted_price !=0:    # fetch discount price of particular product
            percentage = int(((Product_detail.selling_price-Product_detail.discounted_price)/Product_detail.selling_price)*100)
        else:
            percentage = 0
        # ------ code end for caculate percentage ---------
            
        return render(request,'core/Product_details.html',{'pd':Product_detail,'percentage':percentage})


    
 #=========================== Add TO Cart Section =================================================   
def add_to_cart(request, id):    # This 'id' is coming from 'product.id' which hold the id of current product , which is passing through {% url 'addtocart' product.id %} from Product_detail.html 
    if request.user.is_authenticated:
        product = Product.objects.get(pk=id) # product variable is holding data of current object which is passed through 'id' from parameter
        user=request.user                # user variable store the current user i.e steveroger
        Cart(user=user,product=product).save()  # In cart model current user i.e steveroger will save in user variable and current product object will be save in product variable
        return redirect('Productdetails', id)       # finally it will redirect to Product_details.html with current object 'id' to display product after adding to the cart
    else:
        return redirect('login')                # If user is not login it will redirect to login page

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)      # cart_items will fetch product of only current user, and show product available in the cart of the current user.
    print(cart_items)
    return render(request, 'core/cart.html', {'cart_items':cart_items})

def add_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                   
    product.save()
    return redirect('viewcart')

def delete_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('viewcart')


def delete(request,id):
    if request.method == 'POST':
        de = Cart.objects.get(pk=id)
        de.delete()
    return redirect('viewcart')

#===================================== Address ============================================
def address(request):
    if request.method == 'POST':
            print(request.user)
            mf =CustomerForm(request.POST)
            print('mf',mf)
            if mf.is_valid():
                user=request.user                # user variable store the current user i.e steveroger
                name= mf.cleaned_data['name']
                address= mf.cleaned_data['address']
                city= mf.cleaned_data['city']
                state= mf.cleaned_data['state']
                pincode= mf.cleaned_data['pincode']
                print(state)
                print(city)
                print(name)
                Customer(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
                return redirect('address')           
    else:
        mf =CustomerForm()
        address = Customer.objects.filter(user=request.user)
    return render(request,'core/address.html',{'mf':mf,'address':address})


def delete_address(request,id):
    if request.method == 'POST':
        de = Customer.objects.get(pk=id)
        de.delete()
    return redirect('address')

#===================================== Checkout ============================================

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    total =0
    delhivery_charge =2000
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    
    address = Customer.objects.filter(user=request.user)

    return render(request, 'core/checkout.html', {'cart_items': cart_items,'total':total,'final_price':final_price,'address':address})

#===================================== Payment ============================================

def payment(request):

    if request.method == 'POST':
        selected_address_id = request.POST.get('selected_address')

    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    cart_items = Cart.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    total =0
    delhivery_charge =50
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    
    address = Customer.objects.filter(user=request.user)

#=============================== Paypal Code ===============================================
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': final_price,
        'item_name': 'product',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#==========================================================================================================
    return render(request, 'core/payment.html', {'cart_items': cart_items,'total':total,'final_price':final_price,'address':address,'paypal':paypal_payment})

#===================================== Payment Success ============================================

def payment_success(request,selected_address_id):
    print('payment sucess',selected_address_id)   # we have fetch this id from return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}
                                                  # This id contain address detail of particular customer
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Order(user=user,customer=customer_data,product=c.product,quantity=c.quantity).save()
        c.delete()
    return render(request,'core/payment_success.html')


#===================================== Payment Failed ============================================


def payment_failed(request):
    return render(request,'core/payment_failed.html')

#===================================== Order ====================================================

def order(request):
    ord=Order.objects.filter(user=request.user)
    return render(request,'core/order.html',{'ord':ord})