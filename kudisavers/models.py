from django.db import models
from django.utils import timezone
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib.request, urllib.parse, os


# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.prodName



class Category(models.Model):
    Section = models.ForeignKey('Section', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.prodName


class ProductType(models.Model):
    Category = models.ForeignKey('Category', related_name='categories')
    parent = models.ForeignKey('Category', blank=True, null=True, related_name='product_types')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.prodName



class Product(models.Model):
    blockName = models.CharField(max_length=50)
    catName = models.CharField(max_length=50)
    catUrl = models.URLField(max_length=100)
    prodTypeName = models.CharField(max_length=50)
    prodTypeUrl = models.URLField(max_length=100)
    prodName = models.CharField(max_length=50)
    prodUrl = models.URLField(max_length=100)
    prodDesc =  models.TextField(max_length=500)
    prodProperties =  models.TextField(max_length=500)
    reviews = models.TextField()
    imageLink = models.URLField(max_length=100)
    image = models.ImageField()
    offerPrice = models.FloatField()
    availability = models.NullBooleanField(null=True)
    productType = models.ForeignKey('ProductType',
                                  related_name='products', null=True)

    def save(self, *args, **kwargs):
        if self.imageLink:
            filename = urllib.parse(self.imageLink).path.split('/')[-1]
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib.request.urlopen(self.imageLink).read())
            img_temp.flush()
            self.image = File(img_temp)
            super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.prodName


class ProductDetail(models.Model):
     '''
     The ``ProductDetail`` model represents information unique to a
     specific product. This is a generic design that can be used
     to extend the information contained in the ``Product`` model with
     specific, extra details.
     '''
     product = models.ForeignKey('Product',
                                  related_name='details')
     attribute = models.ForeignKey('ProductAttribute')
     value = models.CharField(max_length=500)
     description = models.TextField(blank=True)

     def __unicode__(self):
         return u'%s: %s - %s' % (self.product, self.attribute, self.value)

class ProductAttribute(models.Model):
     '''
     The "ProductAttribute" model represents a class of feature found
     across a set of products. It does not store any data values
     related to the attribute, but only describes what kind of a
     product feature we are trying to capture. Possible attributes
     include things such as materials, colors, sizes, and many, many
     more.
     '''
     name = models.CharField(max_length=300)
     description = models.TextField(blank=True)

     def __unicode__(self):
           return u'%s' % self.name






