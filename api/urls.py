from django.urls import path
from .views import Cartoonize
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('cartoonize/', Cartoonize.as_view(), name="cartoonize+"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)