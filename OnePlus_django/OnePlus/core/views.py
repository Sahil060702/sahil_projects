from django.shortcuts import render

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