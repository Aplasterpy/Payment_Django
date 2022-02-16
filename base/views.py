from typing_extensions import Self
from django.shortcuts import render
from .models import Service
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    if request.method== "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        client = razorpay.Client(auth=('rzp_test_kqC0vdFUau7DbA','Y0GMbjyglBV4QOZTn7L7FY5T'))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        service_data = Service(name = name, amount = amount, payment_id = payment['id'])
        service = Service()
        return render(request, 'index.html',{'payment':payment})
        # print(name,amount)
    return render(request, 'index.html')
@csrf_exempt
def sucess(request):
    if request.method == "POST": 
        data = request.POST
        order_id = ""
        for key , val in data.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        user = Service.objects.filter(order_id = order_id).first()
        user.paid = True
        user.save()
        # print(data)
    return render(request, 'thank.html')