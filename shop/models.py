from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MetalType(models.Model):
    metal_type = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.metal_type

class Category(models.Model):
    metal_type = models.ForeignKey(MetalType)
    c_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.c_name

class Product(models.Model):
    category = models.ForeignKey(Category)
    p_name = models.CharField(max_length = 100)
    p_detail = models.TextField()
    p_cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    p_photo = models.ImageField(blank=True, upload_to='product_photo')

    def __unicode__(self):
        return u'%s - %s: %f ' % (self.p_name, self.category.c_name ,self.p_cost)

class ReviewProduct(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    review = models.TextField()
    rating = models.IntegerField(default = 1)

    def __unicode__(self):
        return u'%s : %s : %s' % (self.user.username, self.product.p_name, self.review)

class ItemPurchase(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    is_purchased = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s : %s ' % (self.user.username, self.product.p_name)

class ShoppingDetail(models.Model):
    full_name = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    town = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    pin = models.IntegerField()

    def __unicode__(self):
        return u'%s : %s %d' %(self.full_name, self.country, self.pin)
