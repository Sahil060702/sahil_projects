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