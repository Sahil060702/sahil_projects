from django.urls import path
from core import views

urlpatterns=[
    path("test/",views.test),
    path("navbar/",views.navbar),
    path("footer/",views.footer),
    path("products/",views.products),
    path("contact/",views.contact),
    path("cart/",views.cart),
    path("account/",views.account),
    #Urls for products on Homepage
    path("buds2/",views.buds2),
    path("nord_buds/",views.nord_buds),
    path("bullets_z2/",views.bullets_z2),
    #Urls for products on Products page
    path("gaming_bundle/",views.gaming_bundle),
    path("charging_bundle/",views.charging_bundle),
    path("music_bundle/",views.music_bundle),
    path("op_12r/",views.op_12r),
    path("op_11r/",views.op_11r),
    path("op_11_5g/",views.op_11_5g),
    path("pad_go/",views.pad_go),
    path("op_pad/",views.op_pad),
    path("folio_case/",views.folio_case),


]