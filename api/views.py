from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, render
from django.urls import reverse
from .utils import send_sms_alert
from django.views.decorators.http import require_http_methods
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView

@api_view(['GET', 'POST'])
def order_list(request):
    #get all orders
    #serialize them
    #return json
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({'orders':serializer.data})
    
    ## Adds orders
    if request.method == "POST":
       serializer = OrderSerializer(data = request.data)
       if serializer.is_valid():
           order = serializer.save()
           #Fetch customer's phone number
           customer = order.customer
           phone_number = customer.phone_number
           message = f"Order received: {order.item} for amount {order.amount} at {order.time}."
           send_sms_alert(phone_number, message)

           return Response(serializer.data, status = status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [IsAuthenticated]

@api_view(['GET', 'POST'])
def customer_list(request):
    #get all customers
    #serialize them
    #return json
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({'customers':serializer.data})

    #Adds customers
    if request.method == "POST":
       serializer = CustomerSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
    permission_classes = [IsAuthenticated]

def home_view(request):
    return render(request, 'home.html')

def oidc_callback(request):
    code = request.GET.get('code')
    error = request.GET.get('error')
    error_description = request.GET.get('error_description')

    if error:
        return render(request, 'home.html', {'error': error, 'error_description': error_description})

    return render(request, 'home.html', {'code': code})

class CustomOIDCCallbackView(OIDCAuthenticationCallbackView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return redirect(reverse('home'))
    