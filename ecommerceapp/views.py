from django.http import HttpResponse
from django.shortcuts import render,redirect
from ecommerceapp.models import Contact,product,Orders,OrderUpdate
from django.contrib import messages
from math import ceil
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm


# Create your views here.
def index(request):
    
     allProds=[]
     catprods= product.objects.values('category', 'id')
     cats= {item["category"] for item in catprods}
     for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

     params={'allProds':allProds }
     return render(request,"index.html", params)


# def productview(request,id):
#     return render(request,"productview.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        
        # Create a contact instance using keyword arguments
        myquery = Contact(name=name, email=email, desc=desc, pnumber=pnumber)
        myquery.save()
        messages.info(request, "We will get back to you soon")
        return render(request, "contact.html")

    return render(request, "contact.html")


def about(request):
    return render(request,"about.html")


def checkout(request):
     if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

     if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json, name=name, amount=amount, email=email, address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, phone=phone)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id, update_desc="the order has been placed")
        update.save()
        thank = True

        #proceess of payment
        order_id ='123'
        host = request.get_host()
        paypal_dict = {
            'business' : settings.PAYPAL_RECEIVER_EMAIL,
            'amount' : '100',
            'item_name': 'Item_Name',
            'invoice': 'INV-123',
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        
        # Redirect to PayPal for payment
        return render(request, 'payment_page.html', {'form': form})

     return HttpResponse("Invalid Request")



@csrf_exempt
def payment_done(request):
    returndata = requsest.POST
    return render(request,'payment_succes.html',{'data':returndata})

@csrf_exempt
def payment_canceled(request):
   
    return render(request,'payment_failed.html') 


#  # # PAYMENT INTEGRATION

#         id = Order.order_id
#         oid=str(id)+"ShopyCart"
#         param_dict = {

#             'MID':keys.MID,
#             'ORDER_ID': oid,
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': email,
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

#         }
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         return render(request, 'paytm.html', {'param_dict': param_dict})

#     return render(request, 'checkout.html')
