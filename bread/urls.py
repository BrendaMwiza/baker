from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    url(r'^bread/$',views.bread,name = 'bread'),
    url(r'^cakes/$',views.cakes,name = 'cakes'),
    url(r'^cookies/$',views.cookies,name = 'cookies'),
    url(r'^snacks/$',views.snacks,name = 'snacks'),
    url(r'^about/$',views.about,name = 'about'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)