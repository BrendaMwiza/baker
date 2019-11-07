from django.db import models

class Categories(models.Model):
      category = models.CharField(max_length=32)
      def save_categories(self):
          self.save()

      def __str__(self):
        return self.category

class Bakery(models.Model):
      name = models.CharField(max_length=32)
      category = models.ForeignKey(Categories,on_delete=models.CASCADE)
      code = models.CharField(max_length=32)
      price = models.IntegerField(default=0)
      post = models.ImageField(upload_to = 'pictures/')

      def save_post(self):
          self.save()

      def __str__(self):
        return self.name

class Order(models.Model):
      name = models.CharField(max_length=32)
      quantity= models.IntegerField(default=0)
      category = models.ForeignKey(Categories,on_delete=models.CASCADE)
      order = models.ImageField(upload_to = 'pictures/')
      phone = models.CharField(max_length=32)

      def save_order(self):
          self.save()