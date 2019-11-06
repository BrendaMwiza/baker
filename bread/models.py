# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categories(models.Model):
      breads = models.ImageField(upload_to = 'pictures/')
      cookier= models.CharField(max_length=32)
      caker= models.CharField(max_length=32)
      pastrier=models.CharField(max_length=32)
      snacks =models.CharField(max_length=30)
      def save_categories(self):
          self.save()
class Post(models.Model):
      code = models.CharField(max_length=32)
      name = models.CharField(max_length=32)
      Categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
      price= models.IntegerField(default=0)
      post = models.ImageField(upload_to = 'pictures/')
class Order(models.Model):
      name = models.CharField(max_length=32)
      post = models.ForeignKey(Post,on_delete=models.CASCADE)
      quantity= models.CharField(max_length=32)
      Categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
      order = models.ImageField(upload_to = 'pictures/')
      zipcode = models.CharField(max_length=32)