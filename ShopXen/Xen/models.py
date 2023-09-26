from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class ChatHistory(models.Model):
    user_query = models.JSONField(default=list)
    bot_response = models.JSONField(default=list)

    def add_user_query(self, query):
        self.user_query.append(query)
        self.save()

    def add_bot_response(self, response):
        self.bot_response.append(response)
        self.save()

    def histoy(self):
        chat=[]

        for i in range(len(self.user_query)):
            chat.append({'User':self.user_query[i], 'Bot':self.bot_response[i]})

        return chat

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    gimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    warranty_period_months = models.PositiveIntegerField()
    return_period_days = models.PositiveIntegerField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    feature_list = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colors = models.CharField(max_length=255)
    weight_grams = models.PositiveIntegerField()
    image_link = models.URLField()
    brand = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @classmethod
    def product(cls, name):
        try:
            return cls.objects.get(name = name)
        except Exception :
            return None
'''
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    warranty_period_months = models.PositiveIntegerField()
    return_period_days = models.PositiveIntegerField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    feature_list = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colors = models.CharField(max_length=255)
    weight_grams = models.PositiveIntegerField()
    image_link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @classmethod
    def product(cls, name):
        try:
            return cls.objects.get(name = name)
        except Exception :
            return None

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Variants(models.Model):
    variant_id = models.AutoField(primary_key=True)
    variant = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=255)

class VariantValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    variant_id = models.ForeignKey(Variants, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=50)

class ProductVariants(models.Model):
    product_variants_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return 'self.variant'

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification_name = models.CharField(max_length=255)
    specification_value = models.TextField()
'''

class Review(models.Model):
    reviews = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
####################################################################################################
 
####################################################################################################
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=15, null=True)
    email = models.TextField()
    phone_number = models.CharField(max_length=15, null=True,)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Cart {self.cart_id} {self.customer_id.username}'

class Wishlist(models.Model):
    wish_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True)
    shipment = models.ForeignKey('Shipment', on_delete=models.SET_NULL, null=True)
    order_data = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Order {self.order_id} - {self.customer_id}"
    
class Order_item(models.Model):
    item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE )
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product_id.name} - {self.item_price}"
    
class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    )
    payment_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f"Payment {self.payment_id} - {self.customer.username} - {self.payment_type}"

class Shipment(models.Model):
    Shipment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return f"Shipment {self.Shipment_id} - {self.customer.username} - {self.address}, {self.city}, {self.country} {self.zip}"
