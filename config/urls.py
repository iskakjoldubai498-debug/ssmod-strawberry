from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # БУЛ ЖЕРДИ ТЕКШЕРИҢИЗ: Башкы беттин жолу болушу керек
    # Мисалы, эгер башкы бетиңиз 'shop' колдонмосунда болсо:
    path('', include('shop.urls')), 
]

# Медиа файлдар үчүн блок (БУЛ ЖЕРДИ ӨЗГӨРТПӨҢҮЗ)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)