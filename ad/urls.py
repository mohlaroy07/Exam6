from django.urls import path
from django.conf import settings
from .views import delete_ad, home_page, ad_detail
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home_page'),
    path('ad/<int:id>/', ad_detail, name='ad_detail'),
    path('delete-ad/<int:id>/',delete_ad, name='delete_ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)