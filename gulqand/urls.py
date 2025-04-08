# gulqand/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gul.urls')),
    path('api/users/',include('users.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)