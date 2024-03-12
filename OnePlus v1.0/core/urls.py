from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('navbar/',views.navbar),
    path('home/',views.home, name='home'),
    path('product/',views.products, name='products'),
    path('aboutus/',views.aboutus, name='about_us'),
    path('cart/',views.cart, name='cart'),
    path('signup/',views.signup, name="signup"),
    path('login/',views.log_in, name="login"),
    path('',views.home, name="home"),
    path('logout/',views.log_out, name="logout"),
    path('product_details/<int:id>/',views.ProductDetailView.as_view(),name='Productdetails'),
    path('view_cart/',views.view_cart, name="viewcart"),
    path('add_to_cart/<int:id>/',views.add_to_cart, name="addtocart"),
    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),
    path('delete_quantity/<int:id>/', views.delete_quantity, name='delete_quantity'),
    path('delete/<int:id>/',views.delete,name='delete'),
    #address
    path('address/',views.address,name='address'),
    #payment
    path('checkout/',views.checkout,name='checkout'),
    path('payment_success/',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
