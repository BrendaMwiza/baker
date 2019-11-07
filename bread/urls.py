from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'home'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^order/',views.order,name='order'),
    url(r'^about/',views.about,name='about'),
    url(r'^orderform', views.order_form, name='orderform'),
]