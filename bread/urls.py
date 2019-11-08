<<<<<<< HEAD
from django.conf.urls import url
=======
from django.conf.urls import url,include
>>>>>>> a49b7d6bd2068c3888052b51a1a4869cb0918bdc
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
<<<<<<< HEAD
    url(r'^$',views.page,name = 'page'),
    url(r'^bread/$',views.bread,name = 'bread'),
    url(r'^cakes/$',views.cakes,name = 'cakes'),
    url(r'^cookies/$',views.cookies,name = 'cookies'),
    url(r'^snacks/$',views.snacks,name = 'snacks'),
    url(r'^about/$',views.about,name = 'about'),
    url(r'^contact/$',views.contact,name = 'contact'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
    url(r'^$',views.index,name = 'home'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^order/',views.order,name='order'),
    url(r'^about/',views.about,name='about'),
    url(r'^orderform', views.order_form, name='orderform'),
]
>>>>>>> a49b7d6bd2068c3888052b51a1a4869cb0918bdc
