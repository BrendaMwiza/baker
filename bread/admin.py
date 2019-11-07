# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categories,Bakery,Order
# Register your models here.

admin.site.register(Categories)
admin.site.register(Bakery)
admin.site.register(Order)