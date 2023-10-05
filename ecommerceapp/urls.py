from django.urls import path,include
from ecommerceapp import views


urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact),
    # path('productview/<int:id>',views.productview,name="productview"),
  
    path('about',views.about,name="about"),
    path('checkout/',views.checkout,name="checkout"),
    path('paypal/',include('paypal.standard.ipn.urls')),
    # path('process-payment/',views.process_payment,name="process_payment"),
    path('payment-done/',views.payment_done,name="payment_done"),
    path('payment-canceled/', views.payment_canceled, name="pay_canceled"),

]
