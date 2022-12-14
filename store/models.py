from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#customer table
class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(max_length=200, blank=True,null=True)
  email = models.EmailField(blank=True, null=True)
  
  def __str__(self):
    return self.name
  
  
#product table
class Product(models.Model):
  name = models.CharField(max_length=200, blank=True,null=True)
  price = models.FloatField()
  digital = models.BooleanField(default=False , blank=True, null=True)
  image = models.ImageField(blank=True,null=True)
  
  def __str__(self):
    return self.name
  
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url
  
#order table

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True,null=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  complete =  models.BooleanField(default=False , blank=True, null=True)
  transaction_id = models.CharField(max_length=200,blank=True, null=True)
  
  def __str__(self):
    return str(self.id)
  
  @property
  def shipping(self):
    shipping = False
    orderitems = self.orderitem_set.all()
    for i in orderitems:
      if i.product.digital == False:
        shipping = True
    return shipping
  
  
  
  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total
  
  @property
  def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total
  
#Order_item

class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
  quantity = models.IntegerField(default=0, blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  @property
  def get_total(self):
    total = self.product.price * self.quantity
    return total
    
    
    
class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
  address = models.CharField(max_length=200, blank=True,null=True)
  city = models.CharField(max_length=200, blank=True,null=True)
  state = models.CharField(max_length=200, blank=True,null=True)
  zipcode = models.CharField(max_length=200, blank=True,null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.address
  
  
  
