from __future__ import unicode_literals

from django.db import models

class Categories(models.Model):
      category = models.CharField(max_length=32)

      def save_categories(self):
          self.save()

class Post(models.Model):
      name = models.CharField(max_length=32)
      category = models.ForeignKey(Categories,on_delete=models.CASCADE)
      code = models.CharField(max_length=32)
      price = models.IntegerField(default=0)
      post = models.ImageField(upload_to = 'pictures/')

      def save_post(self):
          self.save()


class Order(models.Model):
      name = models.CharField(max_length=32)
      post = models.ForeignKey(Post,on_delete=models.CASCADE)
      quantity= models.CharField(max_length=32)
      category = models.ForeignKey(Categories,on_delete=models.CASCADE)
      order = models.ImageField(upload_to = 'pictures/')
      zipcode = models.CharField(max_length=32)
      contacts = models.IntegerField(default=+250)

      def save_order(self):
          self.save()