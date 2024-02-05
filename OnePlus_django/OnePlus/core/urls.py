from django.urls import path
from core import views

urlpatterns=[
    path("test/",views.test),
    path("navbar/",views.navbar),
    path("footer/",views.footer),
    path("products/",views.products),
]