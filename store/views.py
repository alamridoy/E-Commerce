from django.shortcuts import render
from store.models import *
from django.http import JsonResponse
import json
# Create your views here.


def store(request):
  products = Product.objects.all()
  context = {'products':products}
  return render(request,'store/store.html',context)

def cart(request):
  
  if request.user.is_authenticated:
      customer = request.user.customer
      # order, created = Order.objects.get_or_create(customer=customer, complete=False)
      queryset = Order.objects.filter(customer=customer, complete=False)
      if queryset.exists():
        order, created = queryset.first(), False
      else:
        order, created = Order.objects.create(customer=customer, complete=False), True
      items = order.orderitem_set.all()
  else:
      items=[]
      order = {'get_cart_total':0, 'get_cart_items':0}
      
  context = {'order':order,'items':items}
  return render(request,'store/cart.html',context)



def checkout(request):
  if request.user.is_authenticated:
      customer = request.user.customer
      # order, created = Order.objects.get_or_create(customer=customer, complete=False)
      queryset = Order.objects.filter(customer=customer, complete=False)
      if queryset.exists():
        order, created = queryset.first(), False
      else:
        order, created = Order.objects.create(customer=customer, complete=False), True
      items = order.orderitem_set.all()
  else:
      items=[]
      order = {'get_cart_total':0, 'get_cart_items':0}
      
  context = {'order':order,'items':items}
  return render(request,'store/checkout.html',context)

def updateItem(request):
  data = json.loads(request.data)
  productId = data['productId']
  action = data['action']
  
  print('Action:' ,action)
  print('ProductId:', productId)
  return JsonResponse('Item was added', safe=False)

